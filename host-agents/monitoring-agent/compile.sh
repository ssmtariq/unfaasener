g++ -std=c++14 -I .  -I /usr/include/pstreams/ agent.cpp -o monitoringAgent

if [ $? -eq 0 ]; then
    echo "Compilation successful: monitoringAgent created."
else
    echo "Compilation failed."
fi