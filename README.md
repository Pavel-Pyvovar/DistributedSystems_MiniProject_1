# DistributedSystems_MiniProject_1


## Server

Server is responsible for start game initialization (assigning id's, electing a game coordinator) and inter-communication between all client nodes, which are players and a coordinator.

Server is a request/reply distibutor. Each time a player makes a request to a coordinator, server blocks itself until it receives a reply from a coordinator.

Node with the highest id becomes a game leader.

After game starts, each node is notified about it's role. For each role there are some extra information: coordinator is notified about players' ids and symbols, players are notified about their symbols.


## Coordinator

Coordinator is responsible for setting and updating the board. The board is represented in a matrix shape.
Coordinator keeps track on the players' moves (which player moves next, and so on) and checks a winner combination each time after setting a symbol on the board.
Coordinator is also allowed to execute commands simultaniously while it's processing players' requests. It is achieved with multithreading - 1st thread for command execution and 2nd thread for processing players' requests.

## Player

A player is able to run 2 commands: Set-symbol x1,x2 and List-board. In case of winning, a player is notified about a winner. When a player wins, the board state is reset.
