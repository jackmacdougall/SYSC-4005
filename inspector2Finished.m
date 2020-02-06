function inspector2Finished
    global bufferC1W2;
    global bufferC1W3;
    global bufferC2W2;
    global bufferC3W3;
    global componentType;
    global inspector2Blocked;
    global workstation2Production;
    global workstation3Production;
    
    if (bufferC2W2 > 2 && bufferC3W3 > 2)
        inspector2Blocked = true;
        fprintf('Inspector 2 is blocked\n');
    elseif(componentType == 2)
        inspector2Blocked = false;
        if(bufferC2W2 > 2)
            fprintf('Buffer for component 2 full');
        else
            bufferC2W2 = bufferC2W2 + 1;
            fprintf('Component 2 placed in Buffer to Workstation 2\n');
            if (bufferC2W2 ~= 0 && bufferC1W2 ~= 0 && workstation2Production == false)
                bufferC2W2 = bufferC2W2 - 1;
                bufferC1W2 = bufferC1W2 - 1;
                workstation2Production = true;
                fprintf('Workstation 2 Production started\n');
            end 
        end
    elseif (componentType == 3 && bufferC3W3 > 3)
        inspector2Blocked = false;
        if(bufferC3W3 > 2)
            fprintf('Buffer for component 3 full');
        else
            bufferC3W3 = bufferC3W3 + 1;
            fprintf('Component 3 placed in Buffer to Workstation 3\n');
            if (bufferC3W3 ~= 0 && bufferC1W3 ~= 0 && workstation3Production == false)
                bufferC3W3 = bufferC3W3 - 1;
                bufferC1W2 = bufferC1W3 - 1;
                workstation3Production = true;
                fprintf('Workstation 3 Production started\n');
            end 
        end
    end
    
end

