local function copyFileContents(inFile, destFile)
    inFile = "Learning & Testing/Lua/" .. inFile
    destFile = "Learning & Testing/Lua/" .. destFile

    local file = io.open(inFile, "r")
    if file then
        local content = file:read("a")
        local outputFile = io.open(destFile, "w")
        if outputFile then
            outputFile:write(content)
            outputFile:close()
        end
    end
end


copyFileContents("frist.lua", "testDest.lua")