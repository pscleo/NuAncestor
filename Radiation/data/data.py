import numpy as np


def read_file(file, start, end):
  path = "../../Radiation_Simulation/" + file #+ "19300_0/spenvis_gcf.txt"
  with open(path) as f:
      lines = f.readlines()[start:end]  # skip last line

  return np.loadtxt(lines, delimiter=",")




folders = ['28750_0', '28750_20', '28750_40', '23200_0', '23200_20', '23200_40', '19300_0', '19300_20', '19300_40']



def read_folders(file, start, end):
  N = len(folders)
  data_list = []
  for i in range(N):
    data = read_file(folders[i] + "/" + file, start, end)
    data_list.append(data)

  return np.asarray(data_list)



proton_spectrum = read_folders("spenvis_tri.txt", 75, 104)
electron_spectrum = read_folders("spenvis_tri.txt", 180, 209) 
solarprot = read_folders('spenvis_sefflare.txt', 39, 114)
solarprotfluence = read_folders('spenvis_sef.txt', 54, 129)
gcr = read_folders("spenvis_gcf.txt", 91, 182)

let_short = read_folders('spenvis_nlof_srimsi.txt', 89, 1088)
let_long = read_folders('spenvis_nlofl_srimsi.txt', 48, 1047)

let_short_proton = read_folders('spenvis_nlof_srimsi.txt', 1180, 1277)
let_long_proton = read_folders('spenvis_nlofl_srimsi.txt', 1098, 1195)

let_long_mean = read_folders('spenvis_nloll_srimsi.txt', 14, 111)
let_short_mean = read_folders('spenvis_nlol_srimsi.txt', 14, 111)

ionizing_dose = read_folders('spenvis_s2o.txt', 25, 49)
non_ionizing_dose = read_folders('spenvis_nio.txt', 265, 289)



    
    
      
'''let_19300_0 = read_let("19300_0/spenvis_nlof_srimsi.txt", start, end)
let_19300_20 = read_let("19300_20/spenvis_nlof_srimsi.txt", start, end)
let_19300_40 = read_let("19300_40/spenvis_nlof_srimsi.txt", start, end)

let_23200_0 = read_let("23200_0/spenvis_nlof_srimsi.txt", start, end)
let_23200_20 = read_let("23200_20/spenvis_nlof_srimsi.txt", start, end)
let_23200_40 = read_let("23200_40/spenvis_nlof_srimsi.txt", start, end)

let_28750_0 = read_let("28750_0/spenvis_nlof_srimsi.txt", start, end)
let_28750_20 = read_let("28750_20/spenvis_nlof_srimsi.txt", start, end)
let_28750_40 = read_let("28750_40/spenvis_nlof_srimsi.txt", start, end)'''


'''start = 48
end = 1047

let_19300_0_l = read_let("19300_0/spenvis_nlofl_srimsi.txt", start, end)
let_19300_20_l = read_let("19300_20/spenvis_nlofl_srimsi.txt", start, end)
let_19300_40_l = read_let("19300_40/spenvis_nlofl_srimsi.txt", start, end)

let_23200_0_l = read_let("23200_0/spenvis_nlofl_srimsi.txt", start, end)
let_23200_20_l = read_let("23200_20/spenvis_nlofl_srimsi.txt", start, end)
let_23200_40_l = read_let("23200_40/spenvis_nlofl_srimsi.txt", start, end)

let_28750_0_l = read_let("28750_0/spenvis_nlofl_srimsi.txt", start, end)
let_28750_20_l = read_let("28750_20/spenvis_nlofl_srimsi.txt", start, end)
let_28750_40_l = read_let("28750_40/spenvis_nlofl_srimsi.txt", start, end)'''


'''start = 75
end = 104
pflux_19300_0 = read_let("19300_0/spenvis_tri.txt", start, end)
pflux_19300_20 = read_let("19300_20/spenvis_tri.txt", start, end)
pflux_19300_40 = read_let("19300_40/spenvis_tri.txt", start, end)

pflux_23200_0 = read_let("23200_0/spenvis_tri.txt", start, end)
pflux_23200_20 = read_let("23200_20/spenvis_tri.txt", start, end)
pflux_23200_40 = read_let("23200_40/spenvis_tri.txt", start, end)

pflux_28750_0 = read_let("28750_0/spenvis_tri.txt", start, end)
pflux_28750_20 = read_let("28750_20/spenvis_tri.txt", start, end)
pflux_28750_40 = read_let("28750_40/spenvis_tri.txt", start, end)


start = 180
end = 209
eflux_19300_0 = read_let("19300_0/spenvis_tri.txt", start, end)
eflux_19300_20 = read_let("19300_20/spenvis_tri.txt", start, end)
eflux_19300_40 = read_let("19300_40/spenvis_tri.txt", start, end)

eflux_23200_0 = read_let("23200_0/spenvis_tri.txt", start, end)
eflux_23200_20 = read_let("23200_20/spenvis_tri.txt", start, end)
eflux_23200_40 = read_let("19300_40/spenvis_tri.txt", start, end)

eflux_28750_0 = read_let("28750_0/spenvis_tri.txt", start, end)
eflux_28750_20 = read_let("28750_20/spenvis_tri.txt", start, end)
eflux_28750_40 = read_let("28750_40/spenvis_tri.txt", start, end)'''