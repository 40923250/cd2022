-- load pack library
-- must have been added previoulsy in V-REP folder
-- if not done yet, see tutorial ...
require ("pack") 
bpack=string.pack
bunpack=string.unpack

-- define socket
portNb = 33211
serverOn = false
connexionTimeout = 0.001 -- set 1 ms time out
socket=require("socket")
srv = nil
clt1 = nil
nCharMessage = 10

function sysCall_threadmain()
   -- initialization
   -- get left and right motors handles
   leftMotor = sim.getObjectHandle("MotorLeft")
   rightMotor = sim.getObjectHandle("MotorRight")
   -- control loop
   while true do
      -- get simulation time at beginning of the loop
      simTime = sim.getSimulationTime()
      -- if server is not running, start it
      if not serverOn then
	 printToConsole ("not connected")
	 srv = assert(socket.bind('127.0.0.1',portNb))
	 if (srv==nil) then
	    printToConsole ("bad connect")
	 else
	    printToConsole ("get socket")
	    ip, port = srv:getsockname()
	    printToConsole ("server ok at "..ip.." on port "..port)
	    serverOn = true
	    printToConsole ("connexion granted !!! ")
	 end
      end
      -- if server is running, accept command and send back status
      if serverOn then
	 -- to prevent lock on accept, a timeout is set
	 srv:settimeout(connexionTimeout)
	 clt1 = srv:accept()
	 if clt1 ~= nil then
	    -- to prevent lock, a timeout is set
	    --clt1:settimeout(connexionTimeout)
	    -- get the data (command) from the client
	    dataIn = clt1:receive(nCharMessage)
	    if dataIn ~= nil then
	       -- unpack the received data with following format :
	       --   char : first synchro char 'A' 
	       --   char : second synchro char 'Z' 
	       --   float : speed left
	       --   float : speed right
	       nrd1,ch1,ch2,speedLeft,speedRight = bunpack(dataIn,"AAff")
	       if ch1 ~= 'A' or ch2 ~= 'Z' then
		  print ("bad data from py client ...")
	       else
		  -- apply the command
		  sim.setJointTargetVelocity(leftMotor,speedLeft)
		  sim.setJointTargetVelocity(rightMotor,speedRight)
	       end
	       -- prepare the status to send back  the client :
	       -- simulation time and wheel angular position (radians)
	       wheelAngleLeft =  sim.getJointPosition(leftMotor)
	       wheelAngleRight = sim.getJointPosition(rightMotor)
	       ch1 = 'A' -- sync code 1
	       ch2 = 'Z' -- sync code 2
	       -- pack the status data
	       dataPacked = bpack("AAfff",ch1,ch2,simTime,wheelAngleLeft,wheelAngleRight)
	       -- Send the status data back to the client:
	       clt1:send(dataPacked)	 
	    else
	       printToConsole ("no data")
	    end
	    clt1:close()
	 end
      end
   end
end

function sysCall_cleanup()
    -- Put some clean-up code here
end

