% The numbers 1, 2, 3, and 4 correspond to directions.
% 1 corresponds to UP
% 2 corresponds to DOWN
% 3 corresponds to LEFT
% 4 corresponds to RIGHT

% randi(4) returns a random number from 1 through 4
% size(A, 1) returns number of columns

function pgenerator = pgenerator(max_depth)
    in_order = 123456789;

    visited = in_order;

    depth = 0;
    p1 = puzzle(in_order);

    while depth < max_depth
        movement = randi(4);

        if(movement == 1)
            p1 = moveBlankUp(p1);

            alreadyVisited = false;
            for i = 1:size(visited, 1)
                if(visited(i) == p1.state)
                    alreadyVisited = true;
                end
            end

            if(alreadyVisited ~= true)
                visited(length(visited) + 1) = p1.state;
                depth = depth + 1;
            end
        elseif(movement == 2)
            p1 = moveBlankDown(p1);

            alreadyVisited = false;
            for i = 1:size(visited, 1)
                if(visited(i) == p1.state)
                    alreadyVisited = true;
                end
            end

            if(alreadyVisited ~= true)
                visited(length(visited) + 1) = p1.state;
                depth = depth + 1;
            end
        elseif(movement == 3)
            p1 = moveBlankLeft(p1);

            alreadyVisited = false;
            for i = 1:size(visited, 1)
                if(visited(i) == p1.state)
                    alreadyVisited = true;
                end
            end

            if(alreadyVisited ~= true)
                visited(length(visited) + 1) = p1.state;
                depth = depth + 1;
            end
        else
            p1 = moveBlankRight(p1);

            alreadyVisited = false;
            for i = 1:size(visited, 1)
                if(visited(i) == p1.state)
                    alreadyVisited = true;
                end
            end

            if(alreadyVisited ~= true)
                visited(length(visited) + 1) = p1.state;
                depth = depth + 1;
            end
        end
    end %while end  

    pgenerator = p1.state;
end %function end
