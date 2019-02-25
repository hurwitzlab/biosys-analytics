SINGULARITY = /usr/local/bin/singularity
IMG = hello-0.0.1.img
DEF = image.def

clean:
	rm -f $(IMG)

img: clean
	# new syntax
	sudo $(SINGULARITY) create $(IMG) $(DEF)
	# older syntax
	#sudo $(SINGULARITY) create --size 512 $(IMG)
	#sudo $(SINGULARITY) bootstrap $(IMG) $(DEF)

shell:
	sudo $(SINGULARITY) shell --writable -B $(shell pwd):/tmp $(IMG)

run:
	sudo $(SINGULARITY) exec $(IMG) hello.sh
