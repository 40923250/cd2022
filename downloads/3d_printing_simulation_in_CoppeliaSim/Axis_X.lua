Axis_X = {}
local running=0
local home=0
local target=0
local command=""
local Change_Value=0
-------------------------------------------------------------------------------
function Axis_X.set_default(pos_home,pos_running, Val_change)
    home=pos_home
    running=pos_running
    command="home"
    Change_Value=Val_change
end
------------------------------------------------------------------------------
function Axis_X.set_change_value(value)  
    Change_Value=value
end
------------------------------------------------------------------------------
function Axis_X.set_command(cmd)  
     command=cmd
 end
 -------------------------------------------------------------------------------
 function Axis_X.home(pos)  
      x_target=pos
end
-------------------------------------------------------------------------------
function Axis_X.target(pos)  
    target=pos
end
-------------------------------------------------------------------------------
function Axis_X.pos()  
    if(command=="home") then   
        if(running>home) then
       --     running=running+Change_Value              
      --  elseif (running>home) then
            running=running-Change_Value
        else
            command=""
        end   
    end
    --///////////////////////////////////////////
    if(command=="go") then   
        if(running<target-0.002) then
            running=running+Change_Value              
        elseif (running>target+0.002) then
            running=running-Change_Value
        else
            command=""
        end   
    end
    --///////////////////////////////////////////
    return running  
end
-------------------------------------------------------------------------------
function Axis_X.update()
    x_min=0
    x_max=1 
    x_running=0 
end
-------------------------------------------------------------------------------
function Axis_X.set_param(x,y,z)

    print(x,y,z)
end
-------------------------------------------------------------------------------
function Axis_X.foo()
    return x_min
end
-------------------------------------------------------------------------------
function Axis_X.idle()
     if(command=="") then
        return true
     else
        return false
     end
end
-------------------------------------------------------------------------------
return Axis_X