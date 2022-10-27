---
layout: container
name:  "quay.io/biocontainers/pash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pash/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pash/container.yaml"
updated_at: "2022-10-27 01:04:29.983238"
latest: "3.0.6.2--0"
container_url: "https://biocontainers.pro/tools/pash"
aliases:
 - "buildFastaIndex.rb"
 - "convertFastaQualToFastQ.rb"
 - "extractChromLengths.rb"
 - "getRCChrom.rb"
 - "keyFreq"
 - "makeIgnoreList"
 - "pash-3.0lx"
 - "pash2SAM"
 - "pash3.0.rb"
 - "pashToLff.rb"
 - "pprof"
 - "splitFastq.rb"
versions:
 - "3.0.6.2--0"
description: "shpc-registry automated BioContainers addition for pash"
config: {"url": "https://biocontainers.pro/tools/pash", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pash", "latest": {"3.0.6.2--0": "sha256:0755075a8b5078a21e0be5edddf1dbf30b2f911ce1eeb1690cdc14f653594c94"}, "tags": {"3.0.6.2--0": "sha256:0755075a8b5078a21e0be5edddf1dbf30b2f911ce1eeb1690cdc14f653594c94"}, "docker": "quay.io/biocontainers/pash", "aliases": {"buildFastaIndex.rb": "/usr/local/bin/buildFastaIndex.rb", "convertFastaQualToFastQ.rb": "/usr/local/bin/convertFastaQualToFastQ.rb", "extractChromLengths.rb": "/usr/local/bin/extractChromLengths.rb", "getRCChrom.rb": "/usr/local/bin/getRCChrom.rb", "keyFreq": "/usr/local/bin/keyFreq", "makeIgnoreList": "/usr/local/bin/makeIgnoreList", "pash-3.0lx": "/usr/local/bin/pash-3.0lx", "pash2SAM": "/usr/local/bin/pash2SAM", "pash3.0.rb": "/usr/local/bin/pash3.0.rb", "pashToLff.rb": "/usr/local/bin/pashToLff.rb", "pprof": "/usr/local/bin/pprof", "splitFastq.rb": "/usr/local/bin/splitFastq.rb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pash.
shpc-registry automated BioContainers addition for pash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pash:3.0.6.2--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pash/3.0.6.2--0
$ module help quay.io/biocontainers/pash/3.0.6.2--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### buildFastaIndex.rb

```bash
$ singularity exec <container> /usr/local/bin/buildFastaIndex.rb
$ podman run --it --rm --entrypoint /usr/local/bin/buildFastaIndex.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildFastaIndex.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertFastaQualToFastQ.rb

```bash
$ singularity exec <container> /usr/local/bin/convertFastaQualToFastQ.rb
$ podman run --it --rm --entrypoint /usr/local/bin/convertFastaQualToFastQ.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertFastaQualToFastQ.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractChromLengths.rb

```bash
$ singularity exec <container> /usr/local/bin/extractChromLengths.rb
$ podman run --it --rm --entrypoint /usr/local/bin/extractChromLengths.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractChromLengths.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getRCChrom.rb

```bash
$ singularity exec <container> /usr/local/bin/getRCChrom.rb
$ podman run --it --rm --entrypoint /usr/local/bin/getRCChrom.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getRCChrom.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keyFreq

```bash
$ singularity exec <container> /usr/local/bin/keyFreq
$ podman run --it --rm --entrypoint /usr/local/bin/keyFreq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keyFreq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeIgnoreList

```bash
$ singularity exec <container> /usr/local/bin/makeIgnoreList
$ podman run --it --rm --entrypoint /usr/local/bin/makeIgnoreList   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeIgnoreList   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pash-3.0lx

```bash
$ singularity exec <container> /usr/local/bin/pash-3.0lx
$ podman run --it --rm --entrypoint /usr/local/bin/pash-3.0lx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pash-3.0lx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pash2SAM

```bash
$ singularity exec <container> /usr/local/bin/pash2SAM
$ podman run --it --rm --entrypoint /usr/local/bin/pash2SAM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pash2SAM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pash3.0.rb

```bash
$ singularity exec <container> /usr/local/bin/pash3.0.rb
$ podman run --it --rm --entrypoint /usr/local/bin/pash3.0.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pash3.0.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pashToLff.rb

```bash
$ singularity exec <container> /usr/local/bin/pashToLff.rb
$ podman run --it --rm --entrypoint /usr/local/bin/pashToLff.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pashToLff.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pprof

```bash
$ singularity exec <container> /usr/local/bin/pprof
$ podman run --it --rm --entrypoint /usr/local/bin/pprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitFastq.rb

```bash
$ singularity exec <container> /usr/local/bin/splitFastq.rb
$ podman run --it --rm --entrypoint /usr/local/bin/splitFastq.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitFastq.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
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