---
layout: container
name:  "quay.io/biocontainers/virusdetect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/virusdetect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/virusdetect/container.yaml"
updated_at: "2026-06-22 08:05:07.985815"
latest: "2.0.0a0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/virusdetect"
aliases:
 - "binspreader"
 - "pathracer"
 - "pathracer-seq-fs"
 - "spades-gfa-split"
 - "spades-hpc"
 - "virusdetect"
 - "extract_exons.py"
 - "extract_splice_sites.py"
 - "hisat2_read_statistics.py"
 - "hisat2"
 - "hisat2-inspect"
 - "hisat2-inspect-l"
 - "hisat2-inspect-s"
 - "hisat2_extract_exons.py"
 - "hisat2_extract_snps_haplotypes_UCSC.py"
 - "hisat2_extract_snps_haplotypes_VCF.py"
 - "hisat2_extract_splice_sites.py"
 - "hisat2_simulate_reads.py"
 - "hisat2-align-l"
 - "hisat2-align-s"
 - "hisat2-build"
 - "hisat2-build-l"
 - "hisat2-build-s"
 - "coronaspades.py"
 - "metaplasmidspades.py"
 - "metaviralspades.py"
 - "rnaviralspades.py"
 - "velvetg"
 - "velveth"
 - "archive-nlmnlp"
 - "archive-pids"
versions:
 - "2.0.0a0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for virusdetect"
config: {"url": "https://biocontainers.pro/tools/virusdetect", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for virusdetect", "latest": {"2.0.0a0--pyhdfd78af_0": "sha256:7fc54d6f85c734246f192c83a46c8a1978a406499c4135a29d6119b766a485d2"}, "tags": {"2.0.0a0--pyhdfd78af_0": "sha256:7fc54d6f85c734246f192c83a46c8a1978a406499c4135a29d6119b766a485d2"}, "docker": "quay.io/biocontainers/virusdetect", "aliases": {"binspreader": "/usr/local/bin/binspreader", "pathracer": "/usr/local/bin/pathracer", "pathracer-seq-fs": "/usr/local/bin/pathracer-seq-fs", "spades-gfa-split": "/usr/local/bin/spades-gfa-split", "spades-hpc": "/usr/local/bin/spades-hpc", "virusdetect": "/usr/local/bin/virusdetect", "extract_exons.py": "/usr/local/bin/extract_exons.py", "extract_splice_sites.py": "/usr/local/bin/extract_splice_sites.py", "hisat2_read_statistics.py": "/usr/local/bin/hisat2_read_statistics.py", "hisat2": "/usr/local/bin/hisat2", "hisat2-inspect": "/usr/local/bin/hisat2-inspect", "hisat2-inspect-l": "/usr/local/bin/hisat2-inspect-l", "hisat2-inspect-s": "/usr/local/bin/hisat2-inspect-s", "hisat2_extract_exons.py": "/usr/local/bin/hisat2_extract_exons.py", "hisat2_extract_snps_haplotypes_UCSC.py": "/usr/local/bin/hisat2_extract_snps_haplotypes_UCSC.py", "hisat2_extract_snps_haplotypes_VCF.py": "/usr/local/bin/hisat2_extract_snps_haplotypes_VCF.py", "hisat2_extract_splice_sites.py": "/usr/local/bin/hisat2_extract_splice_sites.py", "hisat2_simulate_reads.py": "/usr/local/bin/hisat2_simulate_reads.py", "hisat2-align-l": "/usr/local/bin/hisat2-align-l", "hisat2-align-s": "/usr/local/bin/hisat2-align-s", "hisat2-build": "/usr/local/bin/hisat2-build", "hisat2-build-l": "/usr/local/bin/hisat2-build-l", "hisat2-build-s": "/usr/local/bin/hisat2-build-s", "coronaspades.py": "/usr/local/bin/coronaspades.py", "metaplasmidspades.py": "/usr/local/bin/metaplasmidspades.py", "metaviralspades.py": "/usr/local/bin/metaviralspades.py", "rnaviralspades.py": "/usr/local/bin/rnaviralspades.py", "velvetg": "/usr/local/bin/velvetg", "velveth": "/usr/local/bin/velveth", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/virusdetect.
singularity registry hpc automated addition for virusdetect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/virusdetect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/virusdetect:2.0.0a0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/virusdetect/2.0.0a0--pyhdfd78af_0
$ module help quay.io/biocontainers/virusdetect/2.0.0a0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### virusdetect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### virusdetect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### virusdetect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### virusdetect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### virusdetect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### virusdetect-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### binspreader

```bash
$ singularity exec <container> /usr/local/bin/binspreader
$ podman run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathracer

```bash
$ singularity exec <container> /usr/local/bin/pathracer
$ podman run --it --rm --entrypoint /usr/local/bin/pathracer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathracer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathracer-seq-fs

```bash
$ singularity exec <container> /usr/local/bin/pathracer-seq-fs
$ podman run --it --rm --entrypoint /usr/local/bin/pathracer-seq-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathracer-seq-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gfa-split

```bash
$ singularity exec <container> /usr/local/bin/spades-gfa-split
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-hpc

```bash
$ singularity exec <container> /usr/local/bin/spades-hpc
$ podman run --it --rm --entrypoint /usr/local/bin/spades-hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### virusdetect

```bash
$ singularity exec <container> /usr/local/bin/virusdetect
$ podman run --it --rm --entrypoint /usr/local/bin/virusdetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virusdetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### hisat2_read_statistics.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_read_statistics.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_read_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_read_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2

```bash
$ singularity exec <container> /usr/local/bin/hisat2
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### hisat2_simulate_reads.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_simulate_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### coronaspades.py

```bash
$ singularity exec <container> /usr/local/bin/coronaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaplasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaplasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velvetg

```bash
$ singularity exec <container> /usr/local/bin/velvetg
$ podman run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velveth

```bash
$ singularity exec <container> /usr/local/bin/velveth
$ podman run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nlmnlp

```bash
$ singularity exec <container> /usr/local/bin/archive-nlmnlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pids

```bash
$ singularity exec <container> /usr/local/bin/archive-pids
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
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