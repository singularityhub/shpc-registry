---
layout: container
name:  "quay.io/biocontainers/molpopgen-analysis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/molpopgen-analysis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/molpopgen-analysis/container.yaml"
updated_at: "2024-08-25 02:43:07.984955"
latest: "0.8.8--h733e4d7_9"
container_url: "https://biocontainers.pro/tools/molpopgen-analysis"
aliases:
 - "Fexact"
 - "HBKpermute"
 - "MKtest"
 - "compute"
 - "descPoly"
 - "extractCoding"
 - "gestimator"
 - "kimura80"
 - "polydNdS"
 - "rsq"
 - "sharedPoly"
 - "snntest"
 - "translateCoding"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.8.8--h7fd9d64_8"
 - "0.8.8--h733e4d7_9"
description: "shpc-registry automated BioContainers addition for molpopgen-analysis"
config: {"url": "https://biocontainers.pro/tools/molpopgen-analysis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for molpopgen-analysis", "latest": {"0.8.8--h733e4d7_9": "sha256:6c167975988035ee04e95ff45b625989166a56b00e4631e62170a1a53f3a361c"}, "tags": {"0.8.8--h7fd9d64_8": "sha256:364436e67b67b7633512c1ff898aac1d3836f1608cfa230345b4394d1fbf1c0d", "0.8.8--h733e4d7_9": "sha256:6c167975988035ee04e95ff45b625989166a56b00e4631e62170a1a53f3a361c"}, "docker": "quay.io/biocontainers/molpopgen-analysis", "aliases": {"Fexact": "/usr/local/bin/Fexact", "HBKpermute": "/usr/local/bin/HBKpermute", "MKtest": "/usr/local/bin/MKtest", "compute": "/usr/local/bin/compute", "descPoly": "/usr/local/bin/descPoly", "extractCoding": "/usr/local/bin/extractCoding", "gestimator": "/usr/local/bin/gestimator", "kimura80": "/usr/local/bin/kimura80", "polydNdS": "/usr/local/bin/polydNdS", "rsq": "/usr/local/bin/rsq", "sharedPoly": "/usr/local/bin/sharedPoly", "snntest": "/usr/local/bin/snntest", "translateCoding": "/usr/local/bin/translateCoding", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/molpopgen-analysis.
shpc-registry automated BioContainers addition for molpopgen-analysis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/molpopgen-analysis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/molpopgen-analysis:0.8.8--h733e4d7_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/molpopgen-analysis/0.8.8--h733e4d7_9
$ module help quay.io/biocontainers/molpopgen-analysis/0.8.8--h733e4d7_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### molpopgen-analysis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### molpopgen-analysis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### molpopgen-analysis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### molpopgen-analysis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### molpopgen-analysis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### molpopgen-analysis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Fexact

```bash
$ singularity exec <container> /usr/local/bin/Fexact
$ podman run --it --rm --entrypoint /usr/local/bin/Fexact   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fexact   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HBKpermute

```bash
$ singularity exec <container> /usr/local/bin/HBKpermute
$ podman run --it --rm --entrypoint /usr/local/bin/HBKpermute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HBKpermute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MKtest

```bash
$ singularity exec <container> /usr/local/bin/MKtest
$ podman run --it --rm --entrypoint /usr/local/bin/MKtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MKtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute

```bash
$ singularity exec <container> /usr/local/bin/compute
$ podman run --it --rm --entrypoint /usr/local/bin/compute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### descPoly

```bash
$ singularity exec <container> /usr/local/bin/descPoly
$ podman run --it --rm --entrypoint /usr/local/bin/descPoly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/descPoly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractCoding

```bash
$ singularity exec <container> /usr/local/bin/extractCoding
$ podman run --it --rm --entrypoint /usr/local/bin/extractCoding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractCoding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gestimator

```bash
$ singularity exec <container> /usr/local/bin/gestimator
$ podman run --it --rm --entrypoint /usr/local/bin/gestimator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gestimator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kimura80

```bash
$ singularity exec <container> /usr/local/bin/kimura80
$ podman run --it --rm --entrypoint /usr/local/bin/kimura80   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kimura80   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### polydNdS

```bash
$ singularity exec <container> /usr/local/bin/polydNdS
$ podman run --it --rm --entrypoint /usr/local/bin/polydNdS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/polydNdS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsq

```bash
$ singularity exec <container> /usr/local/bin/rsq
$ podman run --it --rm --entrypoint /usr/local/bin/rsq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sharedPoly

```bash
$ singularity exec <container> /usr/local/bin/sharedPoly
$ podman run --it --rm --entrypoint /usr/local/bin/sharedPoly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sharedPoly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snntest

```bash
$ singularity exec <container> /usr/local/bin/snntest
$ podman run --it --rm --entrypoint /usr/local/bin/snntest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snntest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### translateCoding

```bash
$ singularity exec <container> /usr/local/bin/translateCoding
$ podman run --it --rm --entrypoint /usr/local/bin/translateCoding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/translateCoding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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