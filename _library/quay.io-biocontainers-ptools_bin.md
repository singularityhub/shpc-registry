---
layout: container
name:  "quay.io/biocontainers/ptools_bin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ptools_bin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ptools_bin/container.yaml"
updated_at: "2023-03-31 03:06:59.891739"
latest: "0.0.7--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/ptools_bin"
aliases:
 - "10x_bam2fastq"
 - "compress"
 - "createDiff"
 - "getSeq_genome_wN"
 - "getSeq_genome_woN"
 - "makeBAM.sh"
 - "makeDiff.sh"
 - "makeFastq.sh"
 - "make_unique"
 - "makepBAM_genome.sh"
 - "makepBAM_transcriptome.sh"
 - "pbam2bam"
 - "pbam_mapped_transcriptome"
 - "print_unique"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.0.7--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for ptools_bin"
config: {"url": "https://biocontainers.pro/tools/ptools_bin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ptools_bin", "latest": {"0.0.7--pyh5e36f6f_0": "sha256:2cc59e9ccf72d460836f424dbfe63554d3b9b224c1a2ba3574a5dd110c77310c"}, "tags": {"0.0.7--pyh5e36f6f_0": "sha256:2cc59e9ccf72d460836f424dbfe63554d3b9b224c1a2ba3574a5dd110c77310c"}, "docker": "quay.io/biocontainers/ptools_bin", "aliases": {"10x_bam2fastq": "/usr/local/bin/10x_bam2fastq", "compress": "/usr/local/bin/compress", "createDiff": "/usr/local/bin/createDiff", "getSeq_genome_wN": "/usr/local/bin/getSeq_genome_wN", "getSeq_genome_woN": "/usr/local/bin/getSeq_genome_woN", "makeBAM.sh": "/usr/local/bin/makeBAM.sh", "makeDiff.sh": "/usr/local/bin/makeDiff.sh", "makeFastq.sh": "/usr/local/bin/makeFastq.sh", "make_unique": "/usr/local/bin/make_unique", "makepBAM_genome.sh": "/usr/local/bin/makepBAM_genome.sh", "makepBAM_transcriptome.sh": "/usr/local/bin/makepBAM_transcriptome.sh", "pbam2bam": "/usr/local/bin/pbam2bam", "pbam_mapped_transcriptome": "/usr/local/bin/pbam_mapped_transcriptome", "print_unique": "/usr/local/bin/print_unique", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ptools_bin.
shpc-registry automated BioContainers addition for ptools_bin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ptools_bin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ptools_bin:0.0.7--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ptools_bin/0.0.7--pyh5e36f6f_0
$ module help quay.io/biocontainers/ptools_bin/0.0.7--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ptools_bin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ptools_bin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ptools_bin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ptools_bin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ptools_bin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ptools_bin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 10x_bam2fastq

```bash
$ singularity exec <container> /usr/local/bin/10x_bam2fastq
$ podman run --it --rm --entrypoint /usr/local/bin/10x_bam2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/10x_bam2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compress

```bash
$ singularity exec <container> /usr/local/bin/compress
$ podman run --it --rm --entrypoint /usr/local/bin/compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createDiff

```bash
$ singularity exec <container> /usr/local/bin/createDiff
$ podman run --it --rm --entrypoint /usr/local/bin/createDiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createDiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getSeq_genome_wN

```bash
$ singularity exec <container> /usr/local/bin/getSeq_genome_wN
$ podman run --it --rm --entrypoint /usr/local/bin/getSeq_genome_wN   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getSeq_genome_wN   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getSeq_genome_woN

```bash
$ singularity exec <container> /usr/local/bin/getSeq_genome_woN
$ podman run --it --rm --entrypoint /usr/local/bin/getSeq_genome_woN   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getSeq_genome_woN   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeBAM.sh

```bash
$ singularity exec <container> /usr/local/bin/makeBAM.sh
$ podman run --it --rm --entrypoint /usr/local/bin/makeBAM.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeBAM.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeDiff.sh

```bash
$ singularity exec <container> /usr/local/bin/makeDiff.sh
$ podman run --it --rm --entrypoint /usr/local/bin/makeDiff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeDiff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeFastq.sh

```bash
$ singularity exec <container> /usr/local/bin/makeFastq.sh
$ podman run --it --rm --entrypoint /usr/local/bin/makeFastq.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeFastq.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_unique

```bash
$ singularity exec <container> /usr/local/bin/make_unique
$ podman run --it --rm --entrypoint /usr/local/bin/make_unique   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_unique   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makepBAM_genome.sh

```bash
$ singularity exec <container> /usr/local/bin/makepBAM_genome.sh
$ podman run --it --rm --entrypoint /usr/local/bin/makepBAM_genome.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makepBAM_genome.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makepBAM_transcriptome.sh

```bash
$ singularity exec <container> /usr/local/bin/makepBAM_transcriptome.sh
$ podman run --it --rm --entrypoint /usr/local/bin/makepBAM_transcriptome.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makepBAM_transcriptome.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbam2bam

```bash
$ singularity exec <container> /usr/local/bin/pbam2bam
$ podman run --it --rm --entrypoint /usr/local/bin/pbam2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbam2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbam_mapped_transcriptome

```bash
$ singularity exec <container> /usr/local/bin/pbam_mapped_transcriptome
$ podman run --it --rm --entrypoint /usr/local/bin/pbam_mapped_transcriptome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbam_mapped_transcriptome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print_unique

```bash
$ singularity exec <container> /usr/local/bin/print_unique
$ podman run --it --rm --entrypoint /usr/local/bin/print_unique   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print_unique   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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