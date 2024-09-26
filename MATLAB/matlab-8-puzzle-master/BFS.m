% Breadth First Search algorithm for solving an 8-puzzle.
% Attempts to find the goal state [123456789].
% -- arguments -- 
% start_node: the initial state of the 8-puzzle.
function elapsed_time = BFS(start_node)
tic %start timer
goal = 123456789;
% starting node is the initial state, it has no parent since it is the
% 'root' and has been visitied
start_node.parent = [];
    
queue = start_node;
%visited is a matrix of column arrays where each column is a state that has
%been seen before
visited = [];
queue_index = 1;
while queue_index <= length(queue)
    % pop first element off from queue
    node = queue(queue_index);
    queue_index = queue_index + 1;

    visited(length(visited) + 1) = node.state;
    
    if(node.state == goal)
        reconstruct_path(node);
        elapsed_time = toc % display time elapsed
        return
    else
        %for each possible move add to the queue if it's state has not been
        %visited
        nodeMoveLeft = moveBlankLeft(node);
        if(~ismember(nodeMoveLeft.state, visited))
            nodeMoveLeft.parent = node;
            queue(length(queue) + 1) = nodeMoveLeft;
        end
        
        nodeMoveRight = moveBlankRight(node);
        if(~ismember(nodeMoveRight.state, visited))
            nodeMoveRight.parent = node;
            queue(length(queue) + 1) = nodeMoveRight;
        end
        
        nodeMoveDown = moveBlankDown(node);
        if(~ismember(nodeMoveDown.state, visited))
            nodeMoveDown.parent = node;
            queue(length(queue) + 1) = nodeMoveDown;
        end
        
        nodeMoveUp = moveBlankUp(node);
        if(~ismember(nodeMoveUp.state, visited))
            nodeMoveUp.parent = node;
            queue(length(queue) + 1) = nodeMoveUp;
        end
    end % if end
end % while end
return 
end % function end

                      
                     