# Noise-Removal-with-Autoencoder
Random noise exists in wearable sensor based measurements whose frequency spreads from -&pi; to &pi;. Frequency filtering or smoothing is very likely damage critical information such as QRS. Remove noise from heartbeat using an trained autoencoder could be a promising direction to go as heartbeat is repeatable pattern. The autoencoder is trained using noisy heartbeat as input and corresponding ground truth heartbeat as output. Noise is modeled as uniform distribution. Signal used in the example is sampled at 360 Hz.
 
![Test using normal beats](screenshots/normal_7.png)
![Test using abnormal beats](screenshots/abnormal_7.png)

Noise amplitude has been scaled such that the energy of noise is 70% of signal. 
### Dependency
- Numpy
- Tensorflow
- Matplotlib

### run example
```
~$ git clone
~$ cd /your folder
~$ python3 
```
### More
Under noise condition, detecting heartbeat location becomes more difficult. Combine signal processing with autoencoder will produce more robust result.
- [x] Autoencoder.
- [x] Noise removal on different types of beats assuming R peak correctly detected.
- [ ] Automatic estimating the level of noise.
- [ ] Enable R peak detection using autocoder

