---
layout: container
name:  "quay.io/biocontainers/tritimap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tritimap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tritimap/container.yaml"
updated_at: "2024-01-18 02:58:18.021211"
latest: "0.9.7--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/tritimap"
aliases:
 - "abyss-db-csv"
 - "bioawk"
 - "bwa-mem2"
 - "bwa-mem2.avx"
 - "bwa-mem2.avx2"
 - "bwa-mem2.avx512bw"
 - "bwa-mem2.sse41"
 - "bwa-mem2.sse42"
 - "coronaspades.py"
 - "metaplasmidspades.py"
 - "metaviralspades.py"
 - "rnaviralspades.py"
 - "tritimap"
 - "stone"
 - "bam2bed"
 - "bam2bed-float128"
 - "bam2bed-megarow"
 - "bam2bed-typical"
 - "bam2bed_gnuParallel"
 - "bam2bed_gnuParallel-float128"
 - "bam2bed_gnuParallel-megarow"
 - "bam2bed_gnuParallel-typical"
 - "bam2bed_sge"
versions:
 - "0.9.7--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for tritimap"
config: {"url": "https://biocontainers.pro/tools/tritimap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tritimap", "latest": {"0.9.7--pyh5e36f6f_0": "sha256:8af089aa4982d6f127b5d3adb701ba5345f52ea77f3686c20ba676426e7232c9"}, "tags": {"0.9.7--pyh5e36f6f_0": "sha256:8af089aa4982d6f127b5d3adb701ba5345f52ea77f3686c20ba676426e7232c9"}, "docker": "quay.io/biocontainers/tritimap", "aliases": {"abyss-db-csv": "/usr/local/bin/abyss-db-csv", "bioawk": "/usr/local/bin/bioawk", "bwa-mem2": "/usr/local/bin/bwa-mem2", "bwa-mem2.avx": "/usr/local/bin/bwa-mem2.avx", "bwa-mem2.avx2": "/usr/local/bin/bwa-mem2.avx2", "bwa-mem2.avx512bw": "/usr/local/bin/bwa-mem2.avx512bw", "bwa-mem2.sse41": "/usr/local/bin/bwa-mem2.sse41", "bwa-mem2.sse42": "/usr/local/bin/bwa-mem2.sse42", "coronaspades.py": "/usr/local/bin/coronaspades.py", "metaplasmidspades.py": "/usr/local/bin/metaplasmidspades.py", "metaviralspades.py": "/usr/local/bin/metaviralspades.py", "rnaviralspades.py": "/usr/local/bin/rnaviralspades.py", "tritimap": "/usr/local/bin/tritimap", "stone": "/usr/local/bin/stone", "bam2bed": "/usr/local/bin/bam2bed", "bam2bed-float128": "/usr/local/bin/bam2bed-float128", "bam2bed-megarow": "/usr/local/bin/bam2bed-megarow", "bam2bed-typical": "/usr/local/bin/bam2bed-typical", "bam2bed_gnuParallel": "/usr/local/bin/bam2bed_gnuParallel", "bam2bed_gnuParallel-float128": "/usr/local/bin/bam2bed_gnuParallel-float128", "bam2bed_gnuParallel-megarow": "/usr/local/bin/bam2bed_gnuParallel-megarow", "bam2bed_gnuParallel-typical": "/usr/local/bin/bam2bed_gnuParallel-typical", "bam2bed_sge": "/usr/local/bin/bam2bed_sge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tritimap.
shpc-registry automated BioContainers addition for tritimap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tritimap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tritimap:0.9.7--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tritimap/0.9.7--pyh5e36f6f_0
$ module help quay.io/biocontainers/tritimap/0.9.7--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tritimap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tritimap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tritimap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tritimap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tritimap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tritimap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abyss-db-csv

```bash
$ singularity exec <container> /usr/local/bin/abyss-db-csv
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-db-csv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-db-csv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioawk

```bash
$ singularity exec <container> /usr/local/bin/bioawk
$ podman run --it --rm --entrypoint /usr/local/bin/bioawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx2

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx512bw

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx512bw
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.sse41

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.sse42

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tritimap

```bash
$ singularity exec <container> /usr/local/bin/tritimap
$ podman run --it --rm --entrypoint /usr/local/bin/tritimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tritimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stone

```bash
$ singularity exec <container> /usr/local/bin/stone
$ podman run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed

```bash
$ singularity exec <container> /usr/local/bin/bam2bed
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_sge

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_sge
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
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