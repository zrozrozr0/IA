% Reconstruct and display the path from the given node to the root of the tree.
% -- arguments --
% node: the current node in the tree, must be of class puzzle.

function path = reconstruct_path(node)
    % total_path = current
    % while current in tree
    path(1) = node;
    i = 2;
    
    while ~isempty(node.parent)
        % current = current.parent
        node = node.parent;
        % total_path.append(current)
        path(i) = node;
        i = i + 1;
    end
    
    %print total path
    path = fliplr(path); %flip to get correct descent down tree from initial to goal state

    for i = 1:length(path)
        disp(path(i).state)
    end
end