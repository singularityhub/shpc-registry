---
layout: container
name:  "quay.io/biocontainers/varfish-annotator-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/varfish-annotator-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/varfish-annotator-cli/container.yaml"
updated_at: "2024-05-14 03:04:40.367893"
latest: "0.34--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/varfish-annotator-cli"
aliases:
 - "varfish-annotator"
 - "jaotc"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "jjs"
 - "pack200"
 - "rmic"
versions:
 - "0.9--0"
 - "0.27--hdfd78af_0"
 - "0.26--hdfd78af_0"
 - "0.25--hdfd78af_0"
 - "0.24--hdfd78af_0"
 - "0.23--hdfd78af_0"
 - "0.28--hdfd78af_0"
 - "0.30--hdfd78af_0"
 - "0.29--hdfd78af_0"
 - "0.32--hdfd78af_0"
 - "0.31--hdfd78af_0"
 - "0.34--hdfd78af_0"
 - "0.33--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for varfish-annotator-cli"
config: {"url": "https://biocontainers.pro/tools/varfish-annotator-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for varfish-annotator-cli", "latest": {"0.34--hdfd78af_0": "sha256:bfac20b35aef9da04f930ab067b5081d87db4ae0bcb9c92d917ccd25a8a036a1"}, "tags": {"0.9--0": "sha256:657a6c41bb9517c1fd606579e2dc091a92bd9a0f2c3891d34343de93e2b66467", "0.27--hdfd78af_0": "sha256:778d85820cba2fd4a336e9208d066d66fbe9dbce3286c3e5dd12ee39d695c8eb", "0.26--hdfd78af_0": "sha256:65632fd7e18b0ba98e72398a98b52ecf75526d55faf0640e9f7cc3defaa0ba84", "0.25--hdfd78af_0": "sha256:dd1f080ad7e0b47aa5066455c641ffdb1771358b224423424b8ea35036c6eb06", "0.24--hdfd78af_0": "sha256:976bb0526cd980955c7a740f8941181eaaa2428bbc939c7a6fef91b883e8fbcd", "0.23--hdfd78af_0": "sha256:966cb74572c4451da66e4d499121f0cc4de0a6c554d7d2a06d38fa4b8e4520c3", "0.28--hdfd78af_0": "sha256:747a41cd6e1d13740ef28c42d70fc02199d63e7084b7b778feae8ac1ead41125", "0.30--hdfd78af_0": "sha256:ee9f46690a69d54fe4d6be6ab35692c8ece730c2f17d500d2922e733f05d32ea", "0.29--hdfd78af_0": "sha256:ae2252ee327c57764f18d560910bf6b0ce4a0390087c0aab3008999235af2004", "0.32--hdfd78af_0": "sha256:bc4f15e008a97791d6ca1eac70e2d5b19d2ca2d03a9c62680ec8ea3d470b6859", "0.31--hdfd78af_0": "sha256:09779865c89deaf40c73b8421d21dbe4d5b88ee0ef00439804f26db62e6c22d7", "0.34--hdfd78af_0": "sha256:bfac20b35aef9da04f930ab067b5081d87db4ae0bcb9c92d917ccd25a8a036a1", "0.33--hdfd78af_0": "sha256:b7e989cc33f58efbee31c464b7a9e3c7cb00f8dca396a526090295f229023d5c"}, "docker": "quay.io/biocontainers/varfish-annotator-cli", "aliases": {"varfish-annotator": "/usr/local/bin/varfish-annotator", "jaotc": "/usr/local/bin/jaotc", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "jjs": "/usr/local/bin/jjs", "pack200": "/usr/local/bin/pack200", "rmic": "/usr/local/bin/rmic"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/varfish-annotator-cli.
shpc-registry automated BioContainers addition for varfish-annotator-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/varfish-annotator-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/varfish-annotator-cli:0.34--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/varfish-annotator-cli/0.34--hdfd78af_0
$ module help quay.io/biocontainers/varfish-annotator-cli/0.34--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### varfish-annotator-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### varfish-annotator-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### varfish-annotator-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### varfish-annotator-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### varfish-annotator-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### varfish-annotator-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### varfish-annotator

```bash
$ singularity exec <container> /usr/local/bin/varfish-annotator
$ podman run --it --rm --entrypoint /usr/local/bin/varfish-annotator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varfish-annotator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jjs

```bash
$ singularity exec <container> /usr/local/bin/jjs
$ podman run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pack200

```bash
$ singularity exec <container> /usr/local/bin/pack200
$ podman run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmic

```bash
$ singularity exec <container> /usr/local/bin/rmic
$ podman run --it --rm --entrypoint /usr/local/bin/rmic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmic   -v ${PWD} -w ${PWD} <container> -c " $@"
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