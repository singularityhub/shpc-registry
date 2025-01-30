---
layout: container
name:  "quay.io/biocontainers/moni"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/moni/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/moni/container.yaml"
updated_at: "2025-01-30 03:44:39.363746"
latest: "0.2.2--py310h026fc6c_1"
container_url: "https://biocontainers.pro/tools/moni"
aliases:
 - "SlpEncBuild"
 - "bigbwt"
 - "bigrepair"
 - "build_seqidx"
 - "bwtparse"
 - "bwtparse64"
 - "compress_dictionary"
 - "despair"
 - "extend_ksw2"
 - "idespair"
 - "ipostproc"
 - "iprocdic"
 - "irepair"
 - "largeb_despair"
 - "largeb_idespair"
 - "largeb_irepair"
 - "largeb_repair"
 - "mems"
 - "moni"
 - "ms"
 - "newscan.x"
 - "newscanNT.x"
 - "pfbwt.x"
 - "pfbwt64.x"
 - "pfbwtNT.x"
 - "pfbwtNT64.x"
 - "pfp_thresholds"
 - "pfp_thresholds64"
 - "postproc"
 - "procdic"
 - "pscan.x"
 - "rlebwt_ms_build"
 - "simplebwt"
 - "simplebwt64"
 - "unparse"
 - "remap"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.2.2--py310h3d55dab_0"
 - "0.2.2--py312h9b99d9e_0"
 - "0.2.2--py310h026fc6c_1"
description: "singularity registry hpc automated addition for moni"
config: {"url": "https://biocontainers.pro/tools/moni", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for moni", "latest": {"0.2.2--py310h026fc6c_1": "sha256:6276e3947f52a1f493119ad9196f8647e085a7555f24ca360a4cdf39f466d5ca"}, "tags": {"0.2.2--py310h3d55dab_0": "sha256:c263b48d8c1b10380d7aac920c3d30e2a57b3a512615d5f20609895c4a9619c4", "0.2.2--py312h9b99d9e_0": "sha256:b21bfdfd1e2692369eeb347a759743df8897abc559960df115159d4802bfd623", "0.2.2--py310h026fc6c_1": "sha256:6276e3947f52a1f493119ad9196f8647e085a7555f24ca360a4cdf39f466d5ca"}, "docker": "quay.io/biocontainers/moni", "aliases": {"SlpEncBuild": "/usr/local/bin/SlpEncBuild", "bigbwt": "/usr/local/bin/bigbwt", "bigrepair": "/usr/local/bin/bigrepair", "build_seqidx": "/usr/local/bin/build_seqidx", "bwtparse": "/usr/local/bin/bwtparse", "bwtparse64": "/usr/local/bin/bwtparse64", "compress_dictionary": "/usr/local/bin/compress_dictionary", "despair": "/usr/local/bin/despair", "extend_ksw2": "/usr/local/bin/extend_ksw2", "idespair": "/usr/local/bin/idespair", "ipostproc": "/usr/local/bin/ipostproc", "iprocdic": "/usr/local/bin/iprocdic", "irepair": "/usr/local/bin/irepair", "largeb_despair": "/usr/local/bin/largeb_despair", "largeb_idespair": "/usr/local/bin/largeb_idespair", "largeb_irepair": "/usr/local/bin/largeb_irepair", "largeb_repair": "/usr/local/bin/largeb_repair", "mems": "/usr/local/bin/mems", "moni": "/usr/local/bin/moni", "ms": "/usr/local/bin/ms", "newscan.x": "/usr/local/bin/newscan.x", "newscanNT.x": "/usr/local/bin/newscanNT.x", "pfbwt.x": "/usr/local/bin/pfbwt.x", "pfbwt64.x": "/usr/local/bin/pfbwt64.x", "pfbwtNT.x": "/usr/local/bin/pfbwtNT.x", "pfbwtNT64.x": "/usr/local/bin/pfbwtNT64.x", "pfp_thresholds": "/usr/local/bin/pfp_thresholds", "pfp_thresholds64": "/usr/local/bin/pfp_thresholds64", "postproc": "/usr/local/bin/postproc", "procdic": "/usr/local/bin/procdic", "pscan.x": "/usr/local/bin/pscan.x", "rlebwt_ms_build": "/usr/local/bin/rlebwt_ms_build", "simplebwt": "/usr/local/bin/simplebwt", "simplebwt64": "/usr/local/bin/simplebwt64", "unparse": "/usr/local/bin/unparse", "remap": "/usr/local/bin/remap", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/moni.
singularity registry hpc automated addition for moni
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/moni
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/moni:0.2.2--py310h026fc6c_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/moni/0.2.2--py310h026fc6c_1
$ module help quay.io/biocontainers/moni/0.2.2--py310h026fc6c_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### moni-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### moni-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### moni-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### moni-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### moni-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### moni-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SlpEncBuild

```bash
$ singularity exec <container> /usr/local/bin/SlpEncBuild
$ podman run --it --rm --entrypoint /usr/local/bin/SlpEncBuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SlpEncBuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigbwt

```bash
$ singularity exec <container> /usr/local/bin/bigbwt
$ podman run --it --rm --entrypoint /usr/local/bin/bigbwt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigbwt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigrepair

```bash
$ singularity exec <container> /usr/local/bin/bigrepair
$ podman run --it --rm --entrypoint /usr/local/bin/bigrepair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigrepair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_seqidx

```bash
$ singularity exec <container> /usr/local/bin/build_seqidx
$ podman run --it --rm --entrypoint /usr/local/bin/build_seqidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_seqidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwtparse

```bash
$ singularity exec <container> /usr/local/bin/bwtparse
$ podman run --it --rm --entrypoint /usr/local/bin/bwtparse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwtparse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwtparse64

```bash
$ singularity exec <container> /usr/local/bin/bwtparse64
$ podman run --it --rm --entrypoint /usr/local/bin/bwtparse64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwtparse64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compress_dictionary

```bash
$ singularity exec <container> /usr/local/bin/compress_dictionary
$ podman run --it --rm --entrypoint /usr/local/bin/compress_dictionary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compress_dictionary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### despair

```bash
$ singularity exec <container> /usr/local/bin/despair
$ podman run --it --rm --entrypoint /usr/local/bin/despair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/despair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extend_ksw2

```bash
$ singularity exec <container> /usr/local/bin/extend_ksw2
$ podman run --it --rm --entrypoint /usr/local/bin/extend_ksw2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extend_ksw2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idespair

```bash
$ singularity exec <container> /usr/local/bin/idespair
$ podman run --it --rm --entrypoint /usr/local/bin/idespair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idespair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipostproc

```bash
$ singularity exec <container> /usr/local/bin/ipostproc
$ podman run --it --rm --entrypoint /usr/local/bin/ipostproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipostproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iprocdic

```bash
$ singularity exec <container> /usr/local/bin/iprocdic
$ podman run --it --rm --entrypoint /usr/local/bin/iprocdic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iprocdic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irepair

```bash
$ singularity exec <container> /usr/local/bin/irepair
$ podman run --it --rm --entrypoint /usr/local/bin/irepair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irepair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### largeb_despair

```bash
$ singularity exec <container> /usr/local/bin/largeb_despair
$ podman run --it --rm --entrypoint /usr/local/bin/largeb_despair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/largeb_despair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### largeb_idespair

```bash
$ singularity exec <container> /usr/local/bin/largeb_idespair
$ podman run --it --rm --entrypoint /usr/local/bin/largeb_idespair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/largeb_idespair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### largeb_irepair

```bash
$ singularity exec <container> /usr/local/bin/largeb_irepair
$ podman run --it --rm --entrypoint /usr/local/bin/largeb_irepair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/largeb_irepair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### largeb_repair

```bash
$ singularity exec <container> /usr/local/bin/largeb_repair
$ podman run --it --rm --entrypoint /usr/local/bin/largeb_repair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/largeb_repair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mems

```bash
$ singularity exec <container> /usr/local/bin/mems
$ podman run --it --rm --entrypoint /usr/local/bin/mems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mems   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moni

```bash
$ singularity exec <container> /usr/local/bin/moni
$ podman run --it --rm --entrypoint /usr/local/bin/moni   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moni   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ms

```bash
$ singularity exec <container> /usr/local/bin/ms
$ podman run --it --rm --entrypoint /usr/local/bin/ms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### newscan.x

```bash
$ singularity exec <container> /usr/local/bin/newscan.x
$ podman run --it --rm --entrypoint /usr/local/bin/newscan.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/newscan.x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### newscanNT.x

```bash
$ singularity exec <container> /usr/local/bin/newscanNT.x
$ podman run --it --rm --entrypoint /usr/local/bin/newscanNT.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/newscanNT.x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfbwt.x

```bash
$ singularity exec <container> /usr/local/bin/pfbwt.x
$ podman run --it --rm --entrypoint /usr/local/bin/pfbwt.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfbwt.x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfbwt64.x

```bash
$ singularity exec <container> /usr/local/bin/pfbwt64.x
$ podman run --it --rm --entrypoint /usr/local/bin/pfbwt64.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfbwt64.x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfbwtNT.x

```bash
$ singularity exec <container> /usr/local/bin/pfbwtNT.x
$ podman run --it --rm --entrypoint /usr/local/bin/pfbwtNT.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfbwtNT.x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfbwtNT64.x

```bash
$ singularity exec <container> /usr/local/bin/pfbwtNT64.x
$ podman run --it --rm --entrypoint /usr/local/bin/pfbwtNT64.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfbwtNT64.x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfp_thresholds

```bash
$ singularity exec <container> /usr/local/bin/pfp_thresholds
$ podman run --it --rm --entrypoint /usr/local/bin/pfp_thresholds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfp_thresholds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfp_thresholds64

```bash
$ singularity exec <container> /usr/local/bin/pfp_thresholds64
$ podman run --it --rm --entrypoint /usr/local/bin/pfp_thresholds64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfp_thresholds64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### postproc

```bash
$ singularity exec <container> /usr/local/bin/postproc
$ podman run --it --rm --entrypoint /usr/local/bin/postproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/postproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### procdic

```bash
$ singularity exec <container> /usr/local/bin/procdic
$ podman run --it --rm --entrypoint /usr/local/bin/procdic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/procdic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pscan.x

```bash
$ singularity exec <container> /usr/local/bin/pscan.x
$ podman run --it --rm --entrypoint /usr/local/bin/pscan.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pscan.x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rlebwt_ms_build

```bash
$ singularity exec <container> /usr/local/bin/rlebwt_ms_build
$ podman run --it --rm --entrypoint /usr/local/bin/rlebwt_ms_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rlebwt_ms_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simplebwt

```bash
$ singularity exec <container> /usr/local/bin/simplebwt
$ podman run --it --rm --entrypoint /usr/local/bin/simplebwt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simplebwt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simplebwt64

```bash
$ singularity exec <container> /usr/local/bin/simplebwt64
$ podman run --it --rm --entrypoint /usr/local/bin/simplebwt64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simplebwt64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unparse

```bash
$ singularity exec <container> /usr/local/bin/unparse
$ podman run --it --rm --entrypoint /usr/local/bin/unparse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unparse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remap

```bash
$ singularity exec <container> /usr/local/bin/remap
$ podman run --it --rm --entrypoint /usr/local/bin/remap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remap   -v ${PWD} -w ${PWD} <container> -c " $@"
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