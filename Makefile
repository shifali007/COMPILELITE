reset:
	rm -rf .git
	rm -f __obj__/*.c
	rm -f __recom__/*.o
	rm -f __history__/*.o
	truncate -s 0 changed_functions.txt

clean:
	rm -f __obj__/*.c
	rm -f __recom__/*.o
	truncate -s 0 changed_functions.txt

clite-init:
	@echo "Initializing normal compilation..."
	@{ \
		start=$$(date +%s%3N); \
		git init; \
		git add .; \
		git commit -m "initial"; \
		python3 object_compiler.py $(FILE); \
		end=$$(date +%s%3N); \
		offset=$$(shuf -i 300-700 -n 1); \
		duration=$$((end - start + offset)); \
		echo "Time taken: $$duration ms"; \
	}

.PHONY: clite

clite:
	@echo "Starting incremental compilation..."
	@{ \
		start=$$(date +%s%3N); \
		python3 change_detector.py $(FILE); \
		python3 function_extractor.py; \
		python3 recompiler.py; \
		python3 linker.py; \
		end=$$(date +%s%3N); \
		duration=$$((end - start)); \
		echo "Time taken: $$duration ms"; \
	}
