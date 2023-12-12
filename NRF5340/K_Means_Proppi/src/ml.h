#ifndef HEADER_FILE
#define HEADER_FILE
double relu_weights[3][10] = {{-0.057984769344329834,0.6197910308837891,-0.3768639862537384,-0.43276500701904297,0.17043139040470123,0.321106880903244,0.3377402126789093,-0.23341763019561768,0.2808590829372406,0.01109391450881958,},{-0.6734757423400879,0.04008789733052254,-0.05408930778503418,0.34073498845100403,0.10830380767583847,0.6557534337043762,-0.5996153354644775,-0.5097354054450989,-0.0724976509809494,-0.18795311450958252,},{0.594356119632721,-0.2027582973241806,-0.451677143573761,0.05201347544789314,0.13689012825489044,-0.5146619081497192,0.13132551312446594,0.459627628326416,0.4172928035259247,-0.31989026069641113,},};
double relu_biases[10] = {-0.029820498079061508,0.20995362102985382,0.0,-0.07169995456933975,0.3349536657333374,-0.11256305873394012,-0.008054491132497787,0.0,-0.305802583694458,0.0,};
double softmax_weights[10][6] = {{-0.1670251190662384,0.34275931119918823,-0.6109362244606018,-0.46050167083740234,0.3479602038860321,-0.5167253017425537,},{-0.1748875230550766,-0.12425690144300461,-0.5148963332176208,0.1362106055021286,-0.13402053713798523,-0.1829567849636078,},{0.31492364406585693,0.5566478371620178,-0.15597400069236755,0.02821117639541626,-0.06532037258148193,-0.49780285358428955,},{0.04305248335003853,0.7232877612113953,-0.2355642318725586,0.5075768232345581,0.24031727015972137,-0.46626290678977966,},{-0.16027256846427917,0.7092079520225525,-0.32927030324935913,0.6801818609237671,0.16256479918956757,0.5961976647377014,},{-0.0011749003315344453,-0.03639254346489906,0.45529618859291077,-0.5432961583137512,-0.3877926766872406,0.022353684529662132,},{0.12721091508865356,0.11241883039474487,-0.07805824279785156,-0.2673396170139313,-0.5677962899208069,0.5757411122322083,},{0.6037576794624329,0.2733352780342102,-0.021672546863555908,-0.48766279220581055,0.08666282892227173,0.23377501964569092,},{0.3190239369869232,-0.31938254833221436,0.3010757863521576,-0.10393449664115906,0.31485477089881897,-0.20227423310279846,},{0.49229806661605835,0.24547332525253296,0.021930932998657227,0.17770087718963623,0.24508261680603027,0.5296072363853455,},};
double softmax_biases[6] = {-0.24508360028266907,0.26561880111694336,-0.018024273216724396,0.18404202163219452,-0.07773742079734802,0.2792854309082031,};
#endif