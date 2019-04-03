# RFID_Tag

Chesleah Kribs

Project 2

This project is to be completed either by a group of 2 students or individually.

In this project, you are asked to decode the wireless signal from active RFID tags we have used in our research, collected by my software defined radio device.

An active RFID tag transmits bursts of pulses periodically, where each burst consists of 40 pulses. Each pulse is about 25 micro seconds. The intervals between the pulses are constants. We call the 39 intervals the “signature” of the tag. Different tags have different signatures, and the signatures are used to identify the tags.

The tags do not communicate with each other. When there are multiple tags in the presence, their signal will add up in the air, as we discussed in the class. Usually, as the pulses are so short, their signals are transmitted at different time instants, but there may still be cases in which two pulses overlap in time.

The file with the signatures for all 30 tags, called Proj2_tag_signature, can be found on Canvas. Each line has 39 numbers, which are the interval values for the tag measured in microseconds.

The test data, called Proj2_testdata.gz, can be downloaded from Canvas. Each line is a real number representing the amplitude of the signal at this time instant, called “sample.” A sample is taken every microsecond.

You can use any language you like in this project. The output of your program should be clearly readable, in the format as the sample output of my program on the test data:

burst 1: got tag 7 at 24558

burst 2: got tag 24 at 66729

burst 3: got tag 23 at 224601

burst 4: got tag 3 at 228393

burst 5: got tag 15 at 439384

burst 6: got tag 1 at 601855

burst 7: got tag 4 at 821832

burst 8: got tag 6 at 1042759

burst 9: got tag 5 at 1832627

burst 10: got tag 8 at 2092598

burst 11: got tag 7 at 2171699

burst 12: got tag 24 at 2220087

burst 13: got tag 23 at 2375405

burst 14: got tag 3 at 2380045

burst 15: got tag 15 at 2592555

burst 16: got tag 1 at 2753277

burst 17: got tag 4 at 2973663

burst 18: got tag 6 at 3173450

burst 19: got tag 5 at 3984650

burst 20: got tag 8 at 4245586

burst 21: got tag 7 at 4318839

burst 22: got tag 24 at 4373445

burst 23: got tag 23 at 4526209

burst 24: got tag 3 at 4531697

burst 25: got tag 15 at 4745725

burst 26: got tag 1 at 4883582

burst 27: got tag 4 at 5125494

burst 28: got tag 6 at 5325655

 

In this sample output, the time is measured in microseconds since the beginning of the experiment and is the time when my program sees the rising edge of the first pulse of the burst. I used some additional logic to optimize the edge time detection, which is not required in this project, so if your time differ from mine by a few microseconds, don’t worry about it.

 

You can use any language you like in this project. The output of your program should be clearly readable
