---
layout: container
name:  "quay.io/biocontainers/sra-human-scrubber"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sra-human-scrubber/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sra-human-scrubber/container.yaml"
updated_at: "2023-06-21 03:16:34.695561"
latest: "2.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/sra-human-scrubber"
aliases:
 - "aligns_to"
 - "cut_spots_fastq.py"
 - "fastq_to_fasta.py"
 - "init_db.sh"
 - "scrub.sh"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "2.0.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for sra-human-scrubber"
config: {"url": "https://biocontainers.pro/tools/sra-human-scrubber", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sra-human-scrubber", "latest": {"2.0.0--hdfd78af_0": "sha256:30cb9d414882f518f77fa917196c4df412c3919ecdd4ed4acdf00eb1b70c40ef"}, "tags": {"2.0.0--hdfd78af_0": "sha256:30cb9d414882f518f77fa917196c4df412c3919ecdd4ed4acdf00eb1b70c40ef"}, "docker": "quay.io/biocontainers/sra-human-scrubber", "aliases": {"aligns_to": "/usr/local/bin/aligns_to", "cut_spots_fastq.py": "/usr/local/bin/cut_spots_fastq.py", "fastq_to_fasta.py": "/usr/local/bin/fastq_to_fasta.py", "init_db.sh": "/usr/local/bin/init_db.sh", "scrub.sh": "/usr/local/bin/scrub.sh", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sra-human-scrubber.
shpc-registry automated BioContainers addition for sra-human-scrubber
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sra-human-scrubber
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sra-human-scrubber:2.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sra-human-scrubber/2.0.0--hdfd78af_0
$ module help quay.io/biocontainers/sra-human-scrubber/2.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sra-human-scrubber-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sra-human-scrubber-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sra-human-scrubber-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sra-human-scrubber-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sra-human-scrubber-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sra-human-scrubber-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aligns_to

```bash
$ singularity exec <container> /usr/local/bin/aligns_to
$ podman run --it --rm --entrypoint /usr/local/bin/aligns_to   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aligns_to   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cut_spots_fastq.py

```bash
$ singularity exec <container> /usr/local/bin/cut_spots_fastq.py
$ podman run --it --rm --entrypoint /usr/local/bin/cut_spots_fastq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cut_spots_fastq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/fastq_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### init_db.sh

```bash
$ singularity exec <container> /usr/local/bin/init_db.sh
$ podman run --it --rm --entrypoint /usr/local/bin/init_db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/init_db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scrub.sh

```bash
$ singularity exec <container> /usr/local/bin/scrub.sh
$ podman run --it --rm --entrypoint /usr/local/bin/scrub.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scrub.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)