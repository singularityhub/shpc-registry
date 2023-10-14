---
layout: container
name:  "quay.io/biocontainers/hisat2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hisat2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hisat2/container.yaml"
updated_at: "2023-10-14 03:13:46.754763"
latest: "2.2.1--h87f3376_4"
container_url: "https://biocontainers.pro/tools/hisat2"
aliases:
 - "extract_exons.py"
 - "extract_splice_sites.py"
 - "hisat2"
 - "hisat2-align-l"
 - "hisat2-align-s"
 - "hisat2-build"
 - "hisat2-build-l"
 - "hisat2-build-s"
 - "hisat2-inspect"
 - "hisat2-inspect-l"
 - "hisat2-inspect-s"
 - "hisat2_extract_exons.py"
 - "hisat2_extract_snps_haplotypes_UCSC.py"
 - "hisat2_extract_snps_haplotypes_VCF.py"
 - "hisat2_extract_splice_sites.py"
 - "hisat2_read_statistics.py"
 - "hisat2_simulate_reads.py"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.2.1--h87f3376_4"
description: "shpc-registry automated BioContainers addition for hisat2"
config: {"url": "https://biocontainers.pro/tools/hisat2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hisat2", "latest": {"2.2.1--h87f3376_4": "sha256:21be9c91bf66404e677bc2c70e986e39ce9a40e7950d5034e3561bb992e82ec6"}, "tags": {"2.2.1--h87f3376_4": "sha256:21be9c91bf66404e677bc2c70e986e39ce9a40e7950d5034e3561bb992e82ec6"}, "docker": "quay.io/biocontainers/hisat2", "aliases": {"extract_exons.py": "/usr/local/bin/extract_exons.py", "extract_splice_sites.py": "/usr/local/bin/extract_splice_sites.py", "hisat2": "/usr/local/bin/hisat2", "hisat2-align-l": "/usr/local/bin/hisat2-align-l", "hisat2-align-s": "/usr/local/bin/hisat2-align-s", "hisat2-build": "/usr/local/bin/hisat2-build", "hisat2-build-l": "/usr/local/bin/hisat2-build-l", "hisat2-build-s": "/usr/local/bin/hisat2-build-s", "hisat2-inspect": "/usr/local/bin/hisat2-inspect", "hisat2-inspect-l": "/usr/local/bin/hisat2-inspect-l", "hisat2-inspect-s": "/usr/local/bin/hisat2-inspect-s", "hisat2_extract_exons.py": "/usr/local/bin/hisat2_extract_exons.py", "hisat2_extract_snps_haplotypes_UCSC.py": "/usr/local/bin/hisat2_extract_snps_haplotypes_UCSC.py", "hisat2_extract_snps_haplotypes_VCF.py": "/usr/local/bin/hisat2_extract_snps_haplotypes_VCF.py", "hisat2_extract_splice_sites.py": "/usr/local/bin/hisat2_extract_splice_sites.py", "hisat2_read_statistics.py": "/usr/local/bin/hisat2_read_statistics.py", "hisat2_simulate_reads.py": "/usr/local/bin/hisat2_simulate_reads.py", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hisat2.
shpc-registry automated BioContainers addition for hisat2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hisat2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hisat2:2.2.1--h87f3376_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hisat2/2.2.1--h87f3376_4
$ module help quay.io/biocontainers/hisat2/2.2.1--h87f3376_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hisat2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hisat2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hisat2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hisat2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hisat2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hisat2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### extract_exons.py

```bash
$ singularity exec <container> /usr/local/bin/extract_exons.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_exons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_exons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_splice_sites.py

```bash
$ singularity exec <container> /usr/local/bin/extract_splice_sites.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_splice_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_splice_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2

```bash
$ singularity exec <container> /usr/local/bin/hisat2
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-align-l

```bash
$ singularity exec <container> /usr/local/bin/hisat2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-align-s

```bash
$ singularity exec <container> /usr/local/bin/hisat2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build

```bash
$ singularity exec <container> /usr/local/bin/hisat2-build
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build-l

```bash
$ singularity exec <container> /usr/local/bin/hisat2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build-s

```bash
$ singularity exec <container> /usr/local/bin/hisat2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-inspect

```bash
$ singularity exec <container> /usr/local/bin/hisat2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/hisat2-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/hisat2-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_exons.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_extract_exons.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_extract_exons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_extract_exons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_snps_haplotypes_UCSC.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_extract_snps_haplotypes_UCSC.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_extract_snps_haplotypes_UCSC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_extract_snps_haplotypes_UCSC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_snps_haplotypes_VCF.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_extract_snps_haplotypes_VCF.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_extract_snps_haplotypes_VCF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_extract_snps_haplotypes_VCF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_splice_sites.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_extract_splice_sites.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_extract_splice_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_extract_splice_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_read_statistics.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_read_statistics.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_read_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_read_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_simulate_reads.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_simulate_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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