box = {}

local posX=0
local posY=0
local posZ=0

local lX=1
local wY=1
local hZ=1

local running_X=0
local running_Y=0
local running_Z=0.1
local resolution=0.001

local FSM=0
--___________________________________________________________________________________________________________________________________
 function box.init(length,width,height) 
    lX=length
    wY=width
    hZ=height
    FSM="init"
end
--___________________________________________________________________________________________________________________________________
function box.set_pos(px,py,pz) 
     posX=px
     posY=py
     posZ=pz

     running_X=posX
     running_Y=posY
     running_Z=posZ
end
--___________________________________________________________________________________________________________________________________
function box.reset() 
   -- len=0
   -- width=0
   -- hght=0
    FSM=0
end
--___________________________________________________________________________________________________________________________________
function box.pos() 
    --/////////////////////////
    if(FSM=="init") then
        FSM="1st_side"
    end
    --/////////////////////////
    if(FSM=="1st_side") then    
        running_X =running_X+resolution
        if(running_X>lX) then
        FSM="2nd_side"
        end
    end
    --////////////////////////
    if(FSM=="2nd_side") then
        running_Y =running_Y+resolution
        if(running_Y>wY) then
            running_X=lX
            FSM="3rd_side"
        end
    end
    --////////////////////////
    if(FSM=="3rd_side") then
        running_X =running_X-resolution
        if(running_X<=0) then
            running_Y=wY
            FSM="4th_side"
        end
    end
    --//////////////////////// 
    if(FSM=="4th_side") then
        running_Y =running_Y-resolution
        if(running_Y<0) then
            running_Z=running_Z+.005
            FSM="init"
        end
    end
    --//////////////////////// 
    return running_X, running_Y, running_Z  
end
--___________________________________________________________________________________________________________________________________
 return box