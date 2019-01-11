from enum import Enum


class stationParameters(Enum):
    nu_zenith = 1  # the zenith angle of the incoming neutrino direction
    nu_azimuth = 2  # the azimuth angle of the incoming neutrino direction
    nu_energy = 3  # the energy of the neutrino
    nu_flavor = 4  # the flavor of the neutrino
    ccnc = 5  # neutral current of charged current interaction
    nu_vertex = 6  # the neutrino vertex position
    inelasticity = 7  # inelasiticy ot neutrino interaction
    triggered = 8  # flag if station was triggered or not
    cr_energy = 9  # the cosmic-ray energy
    cr_zenith = 10  # zenith angle of the cosmic-ray incoming direction
    cr_azimuth = 11  # azimuth angle of the cosmic-ray incoming direction
    channels_max_amplitude = 12  # the maximum amplitude of all channels (considered in the trigger module)
    zenith = 13  # the zenith angle of the incoming signal direction (WARNING: this parameter is not well defined as the incoming signal direction might be different for different channels)
    azimuth = 14  # the azimuth angle of the incoming signal direction (WARNING: this parameter is not well defined as the incoming signal direction might be different for different channels)
    zenith_cr_templatefit = 15
    zenith_nu_templatefit = 16
    polarization_angle = 17 # electric field polarization in onsky-coordinates. 0 corresponds to polarization in e_theta, 90deg is polarization in e_phi
    polarization_angle_expectation = 18 # expected polarization based on shower geometry. Defined analogous to polarization_angle
    cr_xcorrelations = 19 # dict of result of crosscorrelations with cr templates
    nu_xcorrelations = 20 #  dict of result of crosscorrelations with nu templates
    station_time = 21
    signal_energy_fluence = 22 # Energy/area in the radio signal
    signal_time = 23
    cr_energy_em = 24  # the electromagnetic shower energy (the cosmic ray energy that ends up in electrons, positrons and gammas)
    cr_spectrum_slope = 25 # Slope of the radio signal's spectrum as reconstructed by the voltageToAnalyticEfieldConverter
    cr_xmax = 26 # Xmax of the air shower
    cr_spectrum_quadratic_term = 27 # result of the second order correction to the spectrum fitted by the voltageToAnalyticEfieldConverter
    cr_energy_em = 28  # the electromagnetic shower energy (the cosmic ray energy that ends up in electrons, positrons and gammas)

class channelParameters(Enum):
    zenith = 1  # zenith angle of the incoming signal direction
    azimuth = 2  # azimuth angle of the incoming signal direction
    maximum_amplitude = 3  # the maximum ampliude of the magnitude of the trace
    SNR = 4  # an dictionary of various signal-to-noise ratio definitions
    maximum_amplitude_envelope = 5  # the maximum ampliude of the hilbert envelope of the trace
    P2P_amplitude = 6  # the peak to peak amplitude
    cr_xcorrelations = 7 # dict of result of crosscorrelations with cr templates
    nu_xcorrelations = 8 #  dict of result of crosscorrelations with nu templates
    
class electricFieldParameters(Enum):
    ray_path_type = 1  # the type of the ray tracing solution ('direct', 'refracted' or 'reflected')
    polarization_angle = 2 # electric field polarization in onsky-coordinates. 0 corresponds to polarization in e_theta, 90deg is polarization in e_phi
    polarization_angle_expectation = 3 # expected polarization based on shower geometry. Defined analogous to polarization_angle
    signal_energy_fluence = 4 # Energy/area in the radio signal
    cr_spectrum_slope = 5 # Slope of the radio signal's spectrum as reconstructed by the voltageToAnalyticEfieldConverter
    zenith = 7  # zenith angle of the signal. Note that refraction at the air/ice boundary is not taken into account
    azimuth = 8  # azimuth angle of the signal. Note that refraction at the air/ice boundary is not taken into account
    signal_time = 9
    nu_vertex_distance = 10 # the distance along the ray path from the vertex to the channel
    nu_viewing_angle = 11 # the angle between shower axis and launch vector
    
    