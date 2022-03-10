local x= require("Axis_X")
local y = require("Axis_Y")
local z=require("Axis_Z")
local box=require("box")

FSM="Wait_For_Home"
x_val=0
y_val=0
z_val=0
count_idle=0;
start_drawing=0
----------------------------------------------------------------------------------------------------------------
function sysCall_init()

  Joint_X=sim.getObjectHandle('Joint_X')
  Joint_Y=sim.getObjectHandle('Joint_Y')
  Joint_Z=sim.getObjectHandle('Joint_Z')
  octree=sim.getObjectHandle("OcTree")
  
  x.set_default(0.03,.25)
  y.set_default(-0.01,.25)
  z.set_default(0.0445,.25)
  box.init(.2,.1,.1)
end
------------------------------------------------------------------------------------------------------------
function sysCall_actuation()

  -------------------------------
  if(FSM=="Wait_For_Home") then
      x_val=x.pos()
      y_val=y.pos()
      z_val=z.pos()
      print("System is Homing...")
          if((x.idle()) or (y.idle()) or (z.idle())) then
              print("System is Now in Home")
              sim.removeVoxelsFromOctree(octree,0,nil)
              start_drawing=1
              FSM="trigger"
          end
  ------------------------------
  elseif(FSM=="trigger") then
  x_val,y_val,z_val=box.pos()
   --  x.target(0.25)
  --  x.set_command("go")
   --   FSM="Waiting_For_Completion"
  ------------------------------
   elseif(FSM=="Waiting_For_Completion") then
          print("Waiting for completion...")
          if(x.idle()) then
              FSM="xx"
          end
  ------------------------------
  else
  print("System is in Idle State>",count_idle)
  count_idle=count_idle+1
  end
  --------------------------------
  print("x=",x_val,"Y=",y_val,"Z=",z_val)

  sim.setJointPosition(Joint_X,x_val)
  sim.setJointPosition(Joint_Y,y_val)
  sim.setJointPosition(Joint_Z,z_val)
  p={x_val-.14,y_val-.05,z_val+.7}
 
  if(start_drawing==1)then
    sim.insertVoxelsIntoOctree(octree,0,p)
    end
end 
-------------------------------------------------------------------------------------------------------------  
function sysCall_sensing()




end
-------------------------------------------------------------------------------------------------------------  
function sysCall_cleanup()
   sim.removeVoxelsFromOctree(octree,0,nil)

end
-------------------------------------------------------------------------------------------------------------  


 

