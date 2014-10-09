
dir_name = '/Users/katiek/Desktop/CurrentCode/MusicFiles/MATfiles/';
load([dir_name,'CoverSongMat.mat'])

for s = [12]
    load([dir_name,'ShingleNumber', num2str(s),'/distmat.mat']);
    
    % Run results for 1-kNNG
    [adj_mat, num_empty_reps, num_poss_matches, ...
        precision_score, recall_score] = ...
        run_results_mutualkNN(dist_mat, 1, 'A', Coversong_mat, s);
    fprintf(['For shingle width ',num2str(s),' and k = ', ...
        num2str(1), ' we have ', num2str(num_poss_matches), ...
        ' possible matches with precision ', ...
        num2str(precision_score), ' and with recall ', ...
        num2str(recall_score), '. There are ', ...
        num2str(num_empty_reps), ' empty representations. \n']);
    adj_save_name = [dir_name, 'ShingleNumber', num2str(s),...
        '/adjmat.mat'];
    save(adj_save_name, 'adj_mat');
    
    % Run results for 10-kNNG, 20-kNNG, 30-kNNG, 40-kNNG, and 50-kNNG.
    for k = [10,20,30,40,50]
        if max(sum(dist_mat >= 0)) >= k
            [adj_mat, num_empty_reps, num_poss_matches, ...
                precision_score, recall_score] = ...
                run_results_mutualkNN(dist_mat, k, 'A', Coversong_mat, s);
            fprintf(['For shingle width ',num2str(s),' and k = ', ...
                num2str(k), ' we have ', num2str(num_poss_matches), ...
                ' possible matches with precision ', ...
                num2str(precision_score), ' and with recall ', ...
                num2str(recall_score), '. \n']);
            adj_save_name = [dir_name, 'ShingleNumber', num2str(s),...
                '/adjmat_k', num2str(k),'.mat'];
            save(adj_save_name, 'adj_mat');
        else
            [adj_mat, num_empty_reps, num_poss_matches, ...
                precision_score, recall_score] = ...
                run_results_mutualkNN(dist_mat, k, 'A', Coversong_mat, s);
            fprintf(['For shingle width ',num2str(s),' and k = ', ...
                num2str(k), ' we have ', num2str(num_poss_matches), ...
                ' possible matches, but we can not make a kNNG. \n']);
        end
        clear adj_mat; clear num_empty_reps; clear num_poss_matches; 
        clear precision_score; clear recall_score;
    end
end