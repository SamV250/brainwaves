import os
import numpy as np
import mne
#Sources: https://medium.com/datatobiz/analyzing-the-brain-waves-data-using-python-9831dd3c0631

#Importing and downloading brain wave data
sample_data_folder = mne.datasets.sample.data_path()
sample_data_evk_file = os.path.join(sample_data_folder, 'MEG', 'sample', 'sample_audvis-ave.fif')
evokeds_list = mne.read_evokeds(sample_data_evk_file, baseline=(None, 0), proj=True, verbose=False)

for e in evokeds_list:
    print(f'Condition:{e.comment}, baseline: {e.baseline}')

#Plotting brain wave data
conds = ('aud/left', 'aud/right', 'vis/left', 'vis/right')
evks = dict(zip(conds,evokeds_list))
evks['aud/left'].plot(exclude=[])

evks['aud/left'].plot(picks='mag', spatial_colors=True, gfp = True)

#Scalp Topography Model
times = np.linspace(0.05, 0.13, 5)
topomap_fig = evks['aud/left'].plot_topomap(ch_type='mag', times=times, colorbar=True)

topomap_fig.savefig("topomap.png")

