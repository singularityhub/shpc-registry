---
layout: container
name:  "quay.io/biocontainers/finestructure"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/finestructure/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/finestructure/container.yaml"
updated_at: "2024-05-06 03:05:39.158939"
latest: "4.1.1--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/finestructure"
aliases:
 - "beagle2chromopainter.pl"
 - "chromopainter2chromopainterv2.pl"
 - "convertrecfile.pl"
 - "fs"
 - "impute2chromopainter.pl"
 - "makeuniformrecfile.pl"
 - "msms2cp.pl"
 - "phasescreen.pl"
 - "phasesubsample.pl"
 - "plink2chromopainter.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.1.3--pl5321h8e5b204_5"
 - "2.1.3--pl5321hd319059_7"
 - "4.1.1--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for finestructure"
config: {"url": "https://biocontainers.pro/tools/finestructure", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for finestructure", "latest": {"4.1.1--pl5321hdfd78af_0": "sha256:de8d57a703646b22834293a6ceb3782447ea50d55cee9abf458db2d2d2342459"}, "tags": {"2.1.3--pl5321h8e5b204_5": "sha256:bdfe16461dfb00fc84851bd0b802a2ec1b21a21cae58bc99f6e65dcf1c411e4e", "2.1.3--pl5321hd319059_7": "sha256:6d60d4ebbbd657fb4cdcde4f9e0acd9454ddcad9f97a9de3277e3aab352ee61e", "4.1.1--pl5321hdfd78af_0": "sha256:de8d57a703646b22834293a6ceb3782447ea50d55cee9abf458db2d2d2342459"}, "docker": "quay.io/biocontainers/finestructure", "aliases": {"beagle2chromopainter.pl": "/usr/local/bin/beagle2chromopainter.pl", "chromopainter2chromopainterv2.pl": "/usr/local/bin/chromopainter2chromopainterv2.pl", "convertrecfile.pl": "/usr/local/bin/convertrecfile.pl", "fs": "/usr/local/bin/fs", "impute2chromopainter.pl": "/usr/local/bin/impute2chromopainter.pl", "makeuniformrecfile.pl": "/usr/local/bin/makeuniformrecfile.pl", "msms2cp.pl": "/usr/local/bin/msms2cp.pl", "phasescreen.pl": "/usr/local/bin/phasescreen.pl", "phasesubsample.pl": "/usr/local/bin/phasesubsample.pl", "plink2chromopainter.pl": "/usr/local/bin/plink2chromopainter.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/finestructure.
shpc-registry automated BioContainers addition for finestructure
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/finestructure
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/finestructure:4.1.1--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/finestructure/4.1.1--pl5321hdfd78af_0
$ module help quay.io/biocontainers/finestructure/4.1.1--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### finestructure-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### finestructure-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### finestructure-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### finestructure-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### finestructure-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### finestructure-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### beagle2chromopainter.pl

```bash
$ singularity exec <container> /usr/local/bin/beagle2chromopainter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/beagle2chromopainter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beagle2chromopainter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chromopainter2chromopainterv2.pl

```bash
$ singularity exec <container> /usr/local/bin/chromopainter2chromopainterv2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/chromopainter2chromopainterv2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chromopainter2chromopainterv2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertrecfile.pl

```bash
$ singularity exec <container> /usr/local/bin/convertrecfile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convertrecfile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertrecfile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fs

```bash
$ singularity exec <container> /usr/local/bin/fs
$ podman run --it --rm --entrypoint /usr/local/bin/fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### impute2chromopainter.pl

```bash
$ singularity exec <container> /usr/local/bin/impute2chromopainter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/impute2chromopainter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impute2chromopainter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeuniformrecfile.pl

```bash
$ singularity exec <container> /usr/local/bin/makeuniformrecfile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makeuniformrecfile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeuniformrecfile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msms2cp.pl

```bash
$ singularity exec <container> /usr/local/bin/msms2cp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/msms2cp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msms2cp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phasescreen.pl

```bash
$ singularity exec <container> /usr/local/bin/phasescreen.pl
$ podman run --it --rm --entrypoint /usr/local/bin/phasescreen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phasescreen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phasesubsample.pl

```bash
$ singularity exec <container> /usr/local/bin/phasesubsample.pl
$ podman run --it --rm --entrypoint /usr/local/bin/phasesubsample.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phasesubsample.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plink2chromopainter.pl

```bash
$ singularity exec <container> /usr/local/bin/plink2chromopainter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/plink2chromopainter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plink2chromopainter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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