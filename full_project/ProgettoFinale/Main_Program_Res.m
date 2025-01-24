fprintf("[MATLAB] Avvio del processo\n");

% Inizializzazione di variabili e caricamento del modello preTrainato

model_path = "/home/jsorel/Desktop/tesi/tuned_networks/ResNet/";
model_name = "ResBinNet2.mat";

model = model_path + model_name;

load(model, "trainedNet");

% Location delle immagini
image_path = "./image/";
image_name = "temp.jpg";

image = image_path + image_name;

% Path del Processo A
path_proc_A = "/home/jsorel/Desktop/tesi/S-MA-R-TLOTER_AI/ProgettoFinale/processo_a/process_a_2.py";

% Path del Processo B
path_proc_B = "/home/jsorel/Desktop/tesi/S-MA-R-TLOTER_AI/ProgettoFinale/processo_b/process_b.py";

% LOOP: 
fprintf("[MATLAB] Avvio del LOOP sistematico \n");
while true
    try
        fprintf("[MATLAB] Avvio del processo A \n");
        % Stringa di avvio del processo A
        avvioProcessoA(path_proc_A, image)

        % Elaborazione con la rete neurale
        % Caricare la nuova immagine
        newImage = imread(image);
        
        % Ridimensionare l'immagine alla dimensione richiesta dalla rete
        inputSize = trainedNet.Layers(1).InputSize;
        resizedImage = imresize(newImage, [inputSize(1) inputSize(2)]);
        
        tic
        % Classificare l'immagine
        [label, scores] = classify(trainedNet, resizedImage);
        elapsed_time = toc;
        % Impaccottamento dei risultati
        forzamento = char(label);
        
        fprintf("forzamento inviato: %s\n", forzamento);

        % Stringa di avvio del processo B
        % con in ingresso l'informazione elaborata
        avvioProcessoB(path_proc_B, forzamento);
        fprintf("Tempo di esecuzione: %fn", elapsed_time);
    catch
        disp("[MATLAB] Loop interrotto manualmente\n");
        break; % Esci dal loop se viene generata un'eccezione
    end
end
