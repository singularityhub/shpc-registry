---
layout: container
name:  "quay.io/biocontainers/illumina-utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/illumina-utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/illumina-utils/container.yaml"
updated_at: "2023-10-05 02:57:09.373392"
latest: "2.12--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/illumina-utils"
aliases:
 - "iu-compute-qual-dicts-from-fastq"
 - "iu-deinterleave-fastq"
 - "iu-demultiplex"
 - "iu-fasta-to-fastq"
 - "iu-fastq-to-fasta"
 - "iu-filter-merged-reads"
 - "iu-filter-quality-bokulich"
 - "iu-filter-quality-minoche"
 - "iu-gen-configs"
 - "iu-gen-matching-fastq-files"
 - "iu-interleave-fastq"
 - "iu-merge-pairs"
 - "iu-remove-ids-from-fastq"
 - "iu-subsample-fastq"
 - "iu-trim-V6-primers"
 - "iu-trim-fastq"
 - "iu-visualize-mismatch-distribution"
 - "iu-visualize-plot-dicts"
 - "iu-visualize-qual-dicts"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
 - "jpgicc"
 - "linkicc"
 - "psicc"
 - "tificc"
versions:
 - "2.9--py_0"
 - "2.12--pyhdfd78af_0"
 - "2.11--py_0"
 - "2.10--py_0"
description: "shpc-registry automated BioContainers addition for illumina-utils"
config: {"url": "https://biocontainers.pro/tools/illumina-utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for illumina-utils", "latest": {"2.12--pyhdfd78af_0": "sha256:66de6b852967a15541c3e6d247694726bd26ec2d3f08d1d04f6768557daf93aa"}, "tags": {"2.9--py_0": "sha256:71bbf576937ace4e755942d2387fef98adf4c1d0ad18babd8937b0d031a02de6", "2.12--pyhdfd78af_0": "sha256:66de6b852967a15541c3e6d247694726bd26ec2d3f08d1d04f6768557daf93aa", "2.11--py_0": "sha256:cf6bdbb6786ceee6dbf003fa3adc640ca4be2e81e35797f40858da82d9db9320", "2.10--py_0": "sha256:1b4fa0cf82e7fd4f3e98dec983fc87ac56b32d75e65927a8c8fc34fe507ca7b6"}, "docker": "quay.io/biocontainers/illumina-utils", "aliases": {"iu-compute-qual-dicts-from-fastq": "/usr/local/bin/iu-compute-qual-dicts-from-fastq", "iu-deinterleave-fastq": "/usr/local/bin/iu-deinterleave-fastq", "iu-demultiplex": "/usr/local/bin/iu-demultiplex", "iu-fasta-to-fastq": "/usr/local/bin/iu-fasta-to-fastq", "iu-fastq-to-fasta": "/usr/local/bin/iu-fastq-to-fasta", "iu-filter-merged-reads": "/usr/local/bin/iu-filter-merged-reads", "iu-filter-quality-bokulich": "/usr/local/bin/iu-filter-quality-bokulich", "iu-filter-quality-minoche": "/usr/local/bin/iu-filter-quality-minoche", "iu-gen-configs": "/usr/local/bin/iu-gen-configs", "iu-gen-matching-fastq-files": "/usr/local/bin/iu-gen-matching-fastq-files", "iu-interleave-fastq": "/usr/local/bin/iu-interleave-fastq", "iu-merge-pairs": "/usr/local/bin/iu-merge-pairs", "iu-remove-ids-from-fastq": "/usr/local/bin/iu-remove-ids-from-fastq", "iu-subsample-fastq": "/usr/local/bin/iu-subsample-fastq", "iu-trim-V6-primers": "/usr/local/bin/iu-trim-V6-primers", "iu-trim-fastq": "/usr/local/bin/iu-trim-fastq", "iu-visualize-mismatch-distribution": "/usr/local/bin/iu-visualize-mismatch-distribution", "iu-visualize-plot-dicts": "/usr/local/bin/iu-visualize-plot-dicts", "iu-visualize-qual-dicts": "/usr/local/bin/iu-visualize-qual-dicts", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config", "jpgicc": "/usr/local/bin/jpgicc", "linkicc": "/usr/local/bin/linkicc", "psicc": "/usr/local/bin/psicc", "tificc": "/usr/local/bin/tificc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/illumina-utils.
shpc-registry automated BioContainers addition for illumina-utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/illumina-utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/illumina-utils:2.12--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/illumina-utils/2.12--pyhdfd78af_0
$ module help quay.io/biocontainers/illumina-utils/2.12--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### illumina-utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### illumina-utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### illumina-utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### illumina-utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### illumina-utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### illumina-utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### iu-compute-qual-dicts-from-fastq

```bash
$ singularity exec <container> /usr/local/bin/iu-compute-qual-dicts-from-fastq
$ podman run --it --rm --entrypoint /usr/local/bin/iu-compute-qual-dicts-from-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-compute-qual-dicts-from-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-deinterleave-fastq

```bash
$ singularity exec <container> /usr/local/bin/iu-deinterleave-fastq
$ podman run --it --rm --entrypoint /usr/local/bin/iu-deinterleave-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-deinterleave-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-demultiplex

```bash
$ singularity exec <container> /usr/local/bin/iu-demultiplex
$ podman run --it --rm --entrypoint /usr/local/bin/iu-demultiplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-demultiplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-fasta-to-fastq

```bash
$ singularity exec <container> /usr/local/bin/iu-fasta-to-fastq
$ podman run --it --rm --entrypoint /usr/local/bin/iu-fasta-to-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-fasta-to-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-fastq-to-fasta

```bash
$ singularity exec <container> /usr/local/bin/iu-fastq-to-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/iu-fastq-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-fastq-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-filter-merged-reads

```bash
$ singularity exec <container> /usr/local/bin/iu-filter-merged-reads
$ podman run --it --rm --entrypoint /usr/local/bin/iu-filter-merged-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-filter-merged-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-filter-quality-bokulich

```bash
$ singularity exec <container> /usr/local/bin/iu-filter-quality-bokulich
$ podman run --it --rm --entrypoint /usr/local/bin/iu-filter-quality-bokulich   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-filter-quality-bokulich   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-filter-quality-minoche

```bash
$ singularity exec <container> /usr/local/bin/iu-filter-quality-minoche
$ podman run --it --rm --entrypoint /usr/local/bin/iu-filter-quality-minoche   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-filter-quality-minoche   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-gen-configs

```bash
$ singularity exec <container> /usr/local/bin/iu-gen-configs
$ podman run --it --rm --entrypoint /usr/local/bin/iu-gen-configs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-gen-configs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-gen-matching-fastq-files

```bash
$ singularity exec <container> /usr/local/bin/iu-gen-matching-fastq-files
$ podman run --it --rm --entrypoint /usr/local/bin/iu-gen-matching-fastq-files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-gen-matching-fastq-files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-interleave-fastq

```bash
$ singularity exec <container> /usr/local/bin/iu-interleave-fastq
$ podman run --it --rm --entrypoint /usr/local/bin/iu-interleave-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-interleave-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-merge-pairs

```bash
$ singularity exec <container> /usr/local/bin/iu-merge-pairs
$ podman run --it --rm --entrypoint /usr/local/bin/iu-merge-pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-merge-pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-remove-ids-from-fastq

```bash
$ singularity exec <container> /usr/local/bin/iu-remove-ids-from-fastq
$ podman run --it --rm --entrypoint /usr/local/bin/iu-remove-ids-from-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-remove-ids-from-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-subsample-fastq

```bash
$ singularity exec <container> /usr/local/bin/iu-subsample-fastq
$ podman run --it --rm --entrypoint /usr/local/bin/iu-subsample-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-subsample-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-trim-V6-primers

```bash
$ singularity exec <container> /usr/local/bin/iu-trim-V6-primers
$ podman run --it --rm --entrypoint /usr/local/bin/iu-trim-V6-primers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-trim-V6-primers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-trim-fastq

```bash
$ singularity exec <container> /usr/local/bin/iu-trim-fastq
$ podman run --it --rm --entrypoint /usr/local/bin/iu-trim-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-trim-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-visualize-mismatch-distribution

```bash
$ singularity exec <container> /usr/local/bin/iu-visualize-mismatch-distribution
$ podman run --it --rm --entrypoint /usr/local/bin/iu-visualize-mismatch-distribution   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-visualize-mismatch-distribution   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-visualize-plot-dicts

```bash
$ singularity exec <container> /usr/local/bin/iu-visualize-plot-dicts
$ podman run --it --rm --entrypoint /usr/local/bin/iu-visualize-plot-dicts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-visualize-plot-dicts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iu-visualize-qual-dicts

```bash
$ singularity exec <container> /usr/local/bin/iu-visualize-qual-dicts
$ podman run --it --rm --entrypoint /usr/local/bin/iu-visualize-qual-dicts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iu-visualize-qual-dicts   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jpgicc

```bash
$ singularity exec <container> /usr/local/bin/jpgicc
$ podman run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linkicc

```bash
$ singularity exec <container> /usr/local/bin/linkicc
$ podman run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psicc

```bash
$ singularity exec <container> /usr/local/bin/psicc
$ podman run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tificc

```bash
$ singularity exec <container> /usr/local/bin/tificc
$ podman run --it --rm --entrypoint /usr/local/bin/tificc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tificc   -v ${PWD} -w ${PWD} <container> -c " $@"
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