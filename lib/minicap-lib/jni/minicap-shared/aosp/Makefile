this_dir = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SOURCES := Android.mk include/Minicap.hpp

all: \
	libs/android-9/armeabi-v7a/minicap.so \
	libs/android-10/armeabi-v7a/minicap.so \
	libs/android-14/armeabi-v7a/minicap.so \
	libs/android-14/x86/minicap.so \
	libs/android-15/armeabi-v7a/minicap.so \
	libs/android-15/x86/minicap.so \
	libs/android-16/armeabi-v7a/minicap.so \
	libs/android-16/x86/minicap.so \
	libs/android-17/armeabi-v7a/minicap.so \
	libs/android-17/x86/minicap.so \
	libs/android-18/armeabi-v7a/minicap.so \
	libs/android-18/x86/minicap.so \
	libs/android-19/armeabi-v7a/minicap.so \
	libs/android-19/x86/minicap.so \
	libs/android-21/armeabi-v7a/minicap.so \
	libs/android-21/arm64-v8a/minicap.so \
	libs/android-21/x86/minicap.so \
	libs/android-21/x86_64/minicap.so \
	libs/android-22/armeabi-v7a/minicap.so \
	libs/android-22/arm64-v8a/minicap.so \
	libs/android-22/x86/minicap.so \
	libs/android-22/x86_64/minicap.so \
	libs/android-23/armeabi-v7a/minicap.so \
	libs/android-23/arm64-v8a/minicap.so \
	libs/android-23/x86/minicap.so \
	libs/android-23/x86_64/minicap.so \
	libs/android-24/armeabi-v7a/minicap.so \
	libs/android-24/arm64-v8a/minicap.so \
	libs/android-24/x86/minicap.so \
	libs/android-24/x86_64/minicap.so \
	libs/android-25/armeabi-v7a/minicap.so \
	libs/android-25/arm64-v8a/minicap.so \
	libs/android-25/x86/minicap.so \
	libs/android-25/x86_64/minicap.so \
	libs/android-26/armeabi-v7a/minicap.so \
	libs/android-26/arm64-v8a/minicap.so \
	libs/android-26/x86/minicap.so \
	libs/android-26/x86_64/minicap.so \
	libs/android-27/armeabi-v7a/minicap.so \
	libs/android-27/arm64-v8a/minicap.so \
	libs/android-27/x86/minicap.so \
	libs/android-27/x86_64/minicap.so \
	libs/android-28/armeabi-v7a/minicap.so \
	libs/android-28/arm64-v8a/minicap.so \
	libs/android-28/x86/minicap.so \
	libs/android-28/x86_64/minicap.so \
	libs/android-29/arm64-v8a/minicap.so \
	libs/android-31/armeabi-v7a/minicap.so \
	libs/android-31/arm64-v8a/minicap.so \
	libs/android-31/x86/minicap.so \
	libs/android-31/x86_64/minicap.so \	

libs/android-9/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_9.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-2.3_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build generic-eng minicap

libs/android-10/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_9.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-2.3.3_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build generic-eng minicap

libs/android-14/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_14.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.0.1_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build full-eng minicap

libs/android-14/x86/minicap.so: $(SOURCES) src/minicap_14.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.0.1_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build full_x86-eng minicap

libs/android-15/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_14.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.0.3_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build full-eng minicap

libs/android-15/x86/minicap.so: $(SOURCES) src/minicap_14.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.0.3_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build full_x86-eng minicap

libs/android-16/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_16.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.1.1_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build full-eng minicap

libs/android-16/x86/minicap.so: $(SOURCES) src/minicap_16.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.1.1_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build full_x86-eng minicap

libs/android-17/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_17.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.2_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build full-eng minicap

libs/android-17/x86/minicap.so: $(SOURCES) src/minicap_17.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.2_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build full_x86-eng minicap

libs/android-18/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_18.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.3_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build aosp_arm-eng minicap

libs/android-18/x86/minicap.so: $(SOURCES) src/minicap_18.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.3_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build aosp_x86-eng minicap

libs/android-19/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_19.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.4_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build aosp_arm-eng minicap

libs/android-19/x86/minicap.so: $(SOURCES) src/minicap_19.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-4.4_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk6 /aosp.sh build aosp_x86-eng minicap

libs/android-21/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_21.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.0.1_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_arm-eng minicap

libs/android-21/arm64-v8a/minicap.so: $(SOURCES) src/minicap_21.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.0.1_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_arm64-eng minicap

libs/android-21/x86/minicap.so: $(SOURCES) src/minicap_21.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.0.1_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_x86-eng minicap

libs/android-21/x86_64/minicap.so: $(SOURCES) src/minicap_21.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.0.1_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_x86_64-eng minicap

libs/android-21/mips/minicap.so: $(SOURCES) src/minicap_21.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.0.1_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_mips-eng minicap

libs/android-21/mips64/minicap.so: $(SOURCES) src/minicap_21.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.0.1_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_mips64-eng minicap

libs/android-22/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_22.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_arm-eng minicap

libs/android-22/arm64-v8a/minicap.so: $(SOURCES) src/minicap_22.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_arm64-eng minicap

libs/android-22/x86/minicap.so: $(SOURCES) src/minicap_22.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_x86-eng minicap

libs/android-22/x86_64/minicap.so: $(SOURCES) src/minicap_22.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_x86_64-eng minicap

libs/android-22/mips/minicap.so: $(SOURCES) src/minicap_22.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_mips-eng minicap

libs/android-22/mips64/minicap.so: $(SOURCES) src/minicap_22.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-5.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_mips64-eng minicap

libs/android-23/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_23.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-6.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_arm-eng minicap

libs/android-23/arm64-v8a/minicap.so: $(SOURCES) src/minicap_23.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-6.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_arm64-eng minicap

libs/android-23/x86/minicap.so: $(SOURCES) src/minicap_23.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-6.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_x86-eng minicap

libs/android-23/x86_64/minicap.so: $(SOURCES) src/minicap_23.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-6.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_x86_64-eng minicap

libs/android-23/mips/minicap.so: $(SOURCES) src/minicap_23.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-6.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_mips-eng minicap

libs/android-23/mips64/minicap.so: $(SOURCES) src/minicap_23.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-6.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk7 /aosp.sh build aosp_mips64-eng minicap

libs/android-24/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_24.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm-eng minicap

libs/android-24/arm64-v8a/minicap.so: $(SOURCES) src/minicap_24.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm64-eng minicap

libs/android-24/x86/minicap.so: $(SOURCES) src/minicap_24.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86-eng minicap

libs/android-24/x86_64/minicap.so: $(SOURCES) src/minicap_24.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86_64-eng minicap

libs/android-24/mips/minicap.so: $(SOURCES) src/minicap_24.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_mips-eng minicap

libs/android-24/mips64/minicap.so: $(SOURCES) src/minicap_24.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_mips64-eng minicap

libs/android-25/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_25.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm-eng minicap

libs/android-25/arm64-v8a/minicap.so: $(SOURCES) src/minicap_25.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm64-eng minicap

libs/android-25/x86/minicap.so: $(SOURCES) src/minicap_25.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86-eng minicap

libs/android-25/x86_64/minicap.so: $(SOURCES) src/minicap_25.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86_64-eng minicap

libs/android-25/mips/minicap.so: $(SOURCES) src/minicap_25.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_mips-eng minicap

libs/android-25/mips64/minicap.so: $(SOURCES) src/minicap_25.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-7.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_mips64-eng minicap

libs/android-26/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_26.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm-eng minicap

libs/android-26/arm64-v8a/minicap.so: $(SOURCES) src/minicap_26.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm64-eng minicap

libs/android-26/x86/minicap.so: $(SOURCES) src/minicap_26.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86-eng minicap

libs/android-26/x86_64/minicap.so: $(SOURCES) src/minicap_26.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86_64-eng minicap

libs/android-26/mips/minicap.so: $(SOURCES) src/minicap_26.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_mips-eng minicap

libs/android-26/mips64/minicap.so: $(SOURCES) src/minicap_26.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_mips64-eng minicap

libs/android-27/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_27.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm-eng minicap

libs/android-27/arm64-v8a/minicap.so: $(SOURCES) src/minicap_27.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm64-eng minicap

libs/android-27/x86/minicap.so: $(SOURCES) src/minicap_27.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86-eng minicap

libs/android-27/x86_64/minicap.so: $(SOURCES) src/minicap_27.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86_64-eng minicap

libs/android-27/mips/minicap.so: $(SOURCES) src/minicap_27.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_mips-eng minicap

libs/android-27/mips64/minicap.so: $(SOURCES) src/minicap_27.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-8.1.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_mips64-eng minicap

libs/android-28/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_28.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-9.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm-eng minicap

libs/android-28/arm64-v8a/minicap.so: $(SOURCES) src/minicap_28.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-9.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm64-eng minicap

libs/android-28/x86/minicap.so: $(SOURCES) src/minicap_28.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-9.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86-eng minicap

libs/android-28/x86_64/minicap.so: $(SOURCES) src/minicap_28.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-9.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86_64-eng minicap

libs/android-28/mips/minicap.so: $(SOURCES) src/minicap_28.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-9.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_mips-eng minicap

libs/android-28/mips64/minicap.so: $(SOURCES) src/minicap_28.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-9.0.0_r1:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_mips64-eng minicap

libs/android-29/arm64-v8a/minicap.so: $(SOURCES) src/minicap_29.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-10.0.0_r2:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm64-eng minicap

libs/android-31/armeabi-v7a/minicap.so: $(SOURCES) src/minicap_31.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-12.0.0_r2:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm-eng minicap

libs/android-31/arm64-v8a/minicap.so: $(SOURCES) src/minicap_31.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-12.0.0_r2:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_arm64-eng minicap

libs/android-31/x86/minicap.so: $(SOURCES) src/minicap_31.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-12.0.0_r2:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86-eng minicap

libs/android-31/x86_64/minicap.so: $(SOURCES) src/minicap_31.cpp
	mkdir -p $(@D)
	docker run --rm \
		-a stdout -a stderr \
		-v /media/aosp/android-12.0.0_r2:/aosp \
		-v $(this_dir):/app \
		-v $(this_dir)$(@D):/artifacts \
		openstf/aosp:jdk8 /aosp.sh build aosp_x86_64-eng minicap