% --- MAIN PROGRAM --- 
% This is the main program that runs through all 100 randomly generated
% states with each algorithm. It records the times taken for each algorithm
% on each initial state and plots the histograms for the algorithms. This
% also returns the mean and variance of each algorithm.
% 
% The initial states were generated using pgenerator(i) where i = 5:29 
% with 4 states being generated at each i.

% clear workspace and command window
clear;
clc;
% preallocate running time arrays for speed
bfs_running_times = zeros(1,100);
dfs_running_times = zeros(1,100);
ids_running_times = zeros(1,100);
a_star_running_times = zeros(1,100);
% load the 100 randomly generated states
load('100-puzzles.mat'); 
for index = 1:100
    current_initial_state = puzzle(puzzles(index)); 
    disp('--- BFS ---')
    disp(index)
    bfs_running_times(index) = BFS(current_initial_state);
    disp('--- DFS ---')
    disp(index)
    dfs_running_times(index) = DFS(current_initial_state);
    disp('--- IDS ---')
    disp(index)
    ids_running_times(index) = IDS(current_initial_state);
    disp('---  A* ---')
    disp(index)
    a_star_running_times(index) = A_star(current_initial_state);
end

figure % plot all histograms on same figure but in different subplots
subplot(2,2,1) % 2x2 subplots
histogram(bfs_running_times)
title('BFS running time distribution')
ylabel('count')
xlabel('running time (sec)')

sprintf('Mean of BFS running times: %.2f', mean(bfs_running_times))
sprintf('Variance of BFS running times: %.2f', var(bfs_running_times))

subplot(2,2,2)
histogram(dfs_running_times)
title('DFS running time distribution')
ylabel('count')
xlabel('running time (sec)')

sprintf('Mean of DFS running times: %.2f', mean(dfs_running_times))
sprintf('Variance of DFS running times: %.2f', var(dfs_running_times))

subplot(2,2,3)
histogram(ids_running_times)
title('IDS running time distribution')
ylabel('count')
xlabel('running time (sec)')

sprintf('Mean of IDS running times: %.2f', mean(ids_running_times))
sprintf('Variance of IDS running times: %.2f', var(ids_running_times))

subplot(2,2,4)
histogram(a_star_running_times)
title('A* running time distribution')
ylabel('count')
xlabel('running time (sec)')

sprintf('Mean of A* running times: %.2f', mean(a_star_running_times))
sprintf('Variance of A* running times: %.2f', var(a_star_running_times))

disp('--- END ---')

