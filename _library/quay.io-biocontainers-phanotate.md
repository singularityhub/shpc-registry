---
layout: container
name:  "quay.io/biocontainers/phanotate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phanotate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phanotate/container.yaml"
updated_at: "2025-11-08 03:20:34.675672"
latest: "1.6.7--py310h184ae93_1"
container_url: "https://biocontainers.pro/tools/phanotate"
aliases:
 - "EukHighConfidenceFilter"
 - "covels-SE"
 - "coves-SE"
 - "eufindtRNA"
 - "fasta2gsi"
 - "phanotate.py"
 - "sstofa"
 - "tRNAscan-SE"
 - "tRNAscan-SE.conf"
 - "trnascan-1.4"
 - "cmalign"
 - "cmbuild"
 - "cmcalibrate"
 - "cmconvert"
 - "cmemit"
 - "cmfetch"
 - "cmpress"
 - "cmscan"
 - "cmsearch"
 - "cmstat"
versions:
 - "1.5.0--hc16433a_2"
 - "1.5.1--hc16433a_0"
 - "1.5.1--h2494328_1"
 - "1.6.4--py38h2494328_0"
 - "1.6.5--py310h0dbaff4_0"
 - "1.5.1--h1f90b4d_1"
 - "1.6.5--py38h2123bcc_1"
 - "1.6.6--py312h28adbb1_0"
 - "1.6.7--py39h2de1943_0"
 - "1.6.7--py310h184ae93_1"
description: "shpc-registry automated BioContainers addition for phanotate"
config: {"url": "https://biocontainers.pro/tools/phanotate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phanotate", "latest": {"1.6.7--py310h184ae93_1": "sha256:028dc4282156235ed14cf778e81368b5c30940dc7f9a0e1ea7bcbe196e4027bf"}, "tags": {"1.5.0--hc16433a_2": "sha256:27e891bbc6ba3809c74389b3871538d751455fe59d69dc4168e5374dd70a4f59", "1.5.1--hc16433a_0": "sha256:e0f97d2fa664f605223b16b34ebdd04e838f6a018d3a367766128020eac9035f", "1.5.1--h2494328_1": "sha256:1b52ae08f4dd57380299b7bbbd49e967a0212849646f184aa34f06691ff8054a", "1.6.4--py38h2494328_0": "sha256:584a0209389dddc95f63be2517f7f389c4b568a20d04b24b870ea1effb66390a", "1.6.5--py310h0dbaff4_0": "sha256:e6d964a0a5c443c9303fffe489ba29784dcefa93ba2bd008758beb81ce65078b", "1.5.1--h1f90b4d_1": "sha256:4fe4209d154a5fdc78b83618593d86a939a7ccc1e144adc0076f76e3ec3d1d35", "1.6.5--py38h2123bcc_1": "sha256:55d31a9a5bc0b7dc95b6847ca15b2c8c90c721dd5f63557f99d6515f1875488c", "1.6.6--py312h28adbb1_0": "sha256:b6bdf6357e422f3875c420f2b881824b25fa394703f68180bde9926359b2b242", "1.6.7--py39h2de1943_0": "sha256:0f8dfda237ba0f9e63a6391ea78dcef53d3d9f03664f76beb6cf3000adc5c0d5", "1.6.7--py310h184ae93_1": "sha256:028dc4282156235ed14cf778e81368b5c30940dc7f9a0e1ea7bcbe196e4027bf"}, "docker": "quay.io/biocontainers/phanotate", "aliases": {"EukHighConfidenceFilter": "/usr/local/bin/EukHighConfidenceFilter", "covels-SE": "/usr/local/bin/covels-SE", "coves-SE": "/usr/local/bin/coves-SE", "eufindtRNA": "/usr/local/bin/eufindtRNA", "fasta2gsi": "/usr/local/bin/fasta2gsi", "phanotate.py": "/usr/local/bin/phanotate.py", "sstofa": "/usr/local/bin/sstofa", "tRNAscan-SE": "/usr/local/bin/tRNAscan-SE", "tRNAscan-SE.conf": "/usr/local/bin/tRNAscan-SE.conf", "trnascan-1.4": "/usr/local/bin/trnascan-1.4", "cmalign": "/usr/local/bin/cmalign", "cmbuild": "/usr/local/bin/cmbuild", "cmcalibrate": "/usr/local/bin/cmcalibrate", "cmconvert": "/usr/local/bin/cmconvert", "cmemit": "/usr/local/bin/cmemit", "cmfetch": "/usr/local/bin/cmfetch", "cmpress": "/usr/local/bin/cmpress", "cmscan": "/usr/local/bin/cmscan", "cmsearch": "/usr/local/bin/cmsearch", "cmstat": "/usr/local/bin/cmstat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phanotate.
shpc-registry automated BioContainers addition for phanotate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phanotate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phanotate:1.6.7--py310h184ae93_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phanotate/1.6.7--py310h184ae93_1
$ module help quay.io/biocontainers/phanotate/1.6.7--py310h184ae93_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phanotate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phanotate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phanotate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phanotate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phanotate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phanotate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### EukHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/EukHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### covels-SE

```bash
$ singularity exec <container> /usr/local/bin/covels-SE
$ podman run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coves-SE

```bash
$ singularity exec <container> /usr/local/bin/coves-SE
$ podman run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eufindtRNA

```bash
$ singularity exec <container> /usr/local/bin/eufindtRNA
$ podman run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2gsi

```bash
$ singularity exec <container> /usr/local/bin/fasta2gsi
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2gsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2gsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phanotate.py

```bash
$ singularity exec <container> /usr/local/bin/phanotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/phanotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phanotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sstofa

```bash
$ singularity exec <container> /usr/local/bin/sstofa
$ podman run --it --rm --entrypoint /usr/local/bin/sstofa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sstofa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscan-SE

```bash
$ singularity exec <container> /usr/local/bin/tRNAscan-SE
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscan-SE.conf

```bash
$ singularity exec <container> /usr/local/bin/tRNAscan-SE.conf
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trnascan-1.4

```bash
$ singularity exec <container> /usr/local/bin/trnascan-1.4
$ podman run --it --rm --entrypoint /usr/local/bin/trnascan-1.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trnascan-1.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmalign

```bash
$ singularity exec <container> /usr/local/bin/cmalign
$ podman run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmbuild

```bash
$ singularity exec <container> /usr/local/bin/cmbuild
$ podman run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmcalibrate

```bash
$ singularity exec <container> /usr/local/bin/cmcalibrate
$ podman run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmconvert

```bash
$ singularity exec <container> /usr/local/bin/cmconvert
$ podman run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmemit

```bash
$ singularity exec <container> /usr/local/bin/cmemit
$ podman run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmfetch

```bash
$ singularity exec <container> /usr/local/bin/cmfetch
$ podman run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpress

```bash
$ singularity exec <container> /usr/local/bin/cmpress
$ podman run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmscan

```bash
$ singularity exec <container> /usr/local/bin/cmscan
$ podman run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmsearch

```bash
$ singularity exec <container> /usr/local/bin/cmsearch
$ podman run --it --rm --entrypoint /usr/local/bin/cmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmstat

```bash
$ singularity exec <container> /usr/local/bin/cmstat
$ podman run --it --rm --entrypoint /usr/local/bin/cmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
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