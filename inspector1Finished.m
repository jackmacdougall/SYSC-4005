function inspector1Finished()
    global bufferC1W1;
    global bufferC1W2;
    global bufferC1W3;
    global bufferC2W2;
    global bufferC3W3;
    global inspector1Blocked;
    global workstation1Production;
    global workstation2Production;
    global workstation3Production;
    global inspector1C1;
    global workstation1;
    global workstation2;
    global workstation3;
    
    if (isBufferFull(bufferC1W1) && isBufferFull(bufferC1W2) && isBufferFull(bufferC1W3))
        inspector1Blocked = true; 
        fprintf('Inspector 1 is blocked\n');       
    else
        inspector1Blocked = false;
        if (numel(bufferC1W1) >= numel(bufferC1W2) && numel(bufferC1W1) >= numel(bufferC1W3))
            bufferC1W1 = bufferC1W1 + 1;
            fprintf('Component 1 placed in Buffer to Workstation 1\n');
            if (numel(bufferC1W1) ~= 0 && workstation1Production == false)
                bufferC1W1 = bufferC1W1 - 1;
                workstation1Production = true;
                fprintf('Workstation 1 Production started\n');
            end
        elseif (numel(bufferC1W2) > numel(bufferC1W1) && numel(bufferC1W2) >= numel(bufferC1W3))
            bufferC1W2 = bufferC1W2 + 1;
            fprintf('Component 1 placed in Buffer to Workstation 2\n');
            if (bufferC1W2 ~= 0 && bufferC2W2 ~= 0 && workstation2Production == false)
                bufferC1W2 = bufferC1W2 - 1;
                bufferC2W2 = bufferC2W2 - 1;
                workstation2Production = true;
                fprintf('Workstation 2 Production started\n');
            end
        else
            bufferC1W3 = bufferC1W3 + 1;
            fprintf('Component 1 placed in Buffer to Workstation 3\n');
            if (numel(bufferC1W3) ~= 0 && numel(bufferC3W3) ~= 0 && workstation3Production == false)
                bufferC1W3 = bufferC1W3 - 1;
                bufferC3W3 = bufferC3W3 - 1;
                workstation3Production = true;
                fprintf('Workstation 3 Production started\n');
            end
        end
       
    end

end

function isFull = isBufferFull(buffer)
    if (buffer == 2)
        isFull = true;
    else
        isFull = false;
    end
end

