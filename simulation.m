function simulation()
    global bufferC1W1;
    global bufferC1W2;
    global bufferC1W3;
    global bufferC2W2;
    global bufferC3W3;
    global workstation1Production;
    global workstation2Production;
    global workstation3Production;
    global inspector1C1;
    global inspector2C2;
    global inspector2C3;
    global workstation1;
    global workstation2;
    global workstation3;
    
    bufferC1W1 = 0;
    bufferC1W2 = 0;
    bufferC1W3 = 0;
    bufferC2W2 = 0;
    bufferC3W3 = 0;
    workstation1Production = false;
    workstation2Production = false;
    workstation3Production = false;
    inspector1C1 = [];
    inspector2C2 = [];
    inspector2C3 = [];
    workstation1 = [];
    workstation2 = [];
    workstation3 = [];
    
    fileId = fopen('servinsp1.dat');
    val = fgetl(fileId);
    while ischar(val)
        inspector1C1 = [inspector1C1 sscanf(val, '%f')];
        val = fgetl(fileId);
    end
    fclose(fileId);
    
    fileId = fopen('servinsp22.dat');
    val = fgetl(fileId);
    while ischar(val)
        inspector2C2 = [inspector2C2 sscanf(val, '%f')];
        val = fgetl(fileId);
    end
    fclose(fileId);
    
    fileId = fopen('servinsp23.dat');
    val = fgetl(fileId);
    while ischar(val)
        inspector2C3 = [inspector2C3 sscanf(val, '%f')];
        val = fgetl(fileId);
    end
    fclose(fileId);
    
    fileId = fopen('ws1.dat');
    val = fgetl(fileId);
    while ischar(val)
        workstation1 = [workstation1 sscanf(val, '%f')];
        val = fgetl(fileId);
    end
    fclose(fileId);
    
    fileId = fopen('ws2.dat');
    val = fgetl(fileId);
    while ischar(val)
        workstation2 = [workstation2 sscanf(val, '%f')];
        val = fgetl(fileId);
    end
    
    fclose(fileId);
    fileId = fopen('ws3.dat');
    val = fgetl(fileId);
    while ischar(val)
        workstation3 = [workstation3 sscanf(val, '%f')];
        val = fgetl(fileId);
    end
    fclose(fileId);
    
end

