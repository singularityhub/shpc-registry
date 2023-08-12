---
layout: container
name:  "quay.io/biocontainers/trtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trtools/container.yaml"
updated_at: "2023-08-12 02:41:27.242784"
latest: "5.0.2--pyhdec4592_0"
container_url: "https://biocontainers.pro/tools/trtools"
aliases:
 - "compareSTR"
 - "dumpSTR"
 - "mergeSTR"
 - "qcSTR"
 - "statSTR"
 - "test_trtools.sh"
 - "trtools_prep_beagle_vcf.sh"
 - "cyvcf2"
 - "coloredlogs"
 - "humanfriendly"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "shiftBed"
 - "annotateBed"
versions:
 - "4.2.1--pyhb765511_0"
 - "5.0.1--pyha447b20_0"
 - "5.0.2--pyhdec4592_0"
description: "shpc-registry automated BioContainers addition for trtools"
config: {"url": "https://biocontainers.pro/tools/trtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trtools", "latest": {"5.0.2--pyhdec4592_0": "sha256:be85e708d87a71b06cc78fcbe78faaf605b9272d7dd021adcd578016e3e242b7"}, "tags": {"4.2.1--pyhb765511_0": "sha256:503e5b4beab6b212fdd777e59cc6f84b944d63665105b77d0e3374d8391d498a", "5.0.1--pyha447b20_0": "sha256:49cffe81a292596cd640c6bf49779d5a8480785e5c844ba4af8de0ad7528c4a3", "5.0.2--pyhdec4592_0": "sha256:be85e708d87a71b06cc78fcbe78faaf605b9272d7dd021adcd578016e3e242b7"}, "docker": "quay.io/biocontainers/trtools", "aliases": {"compareSTR": "/usr/local/bin/compareSTR", "dumpSTR": "/usr/local/bin/dumpSTR", "mergeSTR": "/usr/local/bin/mergeSTR", "qcSTR": "/usr/local/bin/qcSTR", "statSTR": "/usr/local/bin/statSTR", "test_trtools.sh": "/usr/local/bin/test_trtools.sh", "trtools_prep_beagle_vcf.sh": "/usr/local/bin/trtools_prep_beagle_vcf.sh", "cyvcf2": "/usr/local/bin/cyvcf2", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trtools.
shpc-registry automated BioContainers addition for trtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trtools:5.0.2--pyhdec4592_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trtools/5.0.2--pyhdec4592_0
$ module help quay.io/biocontainers/trtools/5.0.2--pyhdec4592_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compareSTR

```bash
$ singularity exec <container> /usr/local/bin/compareSTR
$ podman run --it --rm --entrypoint /usr/local/bin/compareSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compareSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpSTR

```bash
$ singularity exec <container> /usr/local/bin/dumpSTR
$ podman run --it --rm --entrypoint /usr/local/bin/dumpSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeSTR

```bash
$ singularity exec <container> /usr/local/bin/mergeSTR
$ podman run --it --rm --entrypoint /usr/local/bin/mergeSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qcSTR

```bash
$ singularity exec <container> /usr/local/bin/qcSTR
$ podman run --it --rm --entrypoint /usr/local/bin/qcSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statSTR

```bash
$ singularity exec <container> /usr/local/bin/statSTR
$ podman run --it --rm --entrypoint /usr/local/bin/statSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_trtools.sh

```bash
$ singularity exec <container> /usr/local/bin/test_trtools.sh
$ podman run --it --rm --entrypoint /usr/local/bin/test_trtools.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_trtools.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trtools_prep_beagle_vcf.sh

```bash
$ singularity exec <container> /usr/local/bin/trtools_prep_beagle_vcf.sh
$ podman run --it --rm --entrypoint /usr/local/bin/trtools_prep_beagle_vcf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trtools_prep_beagle_vcf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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