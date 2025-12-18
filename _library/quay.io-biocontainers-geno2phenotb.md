---
layout: container
name:  "quay.io/biocontainers/geno2phenotb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/geno2phenotb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/geno2phenotb/container.yaml"
updated_at: "2025-12-18 04:04:33.879612"
latest: "1.0.1--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/geno2phenotb"
aliases:
 - "GenomeAnalysisTK"
 - "MTBseq"
 - "gatk3"
 - "geno2phenotb"
 - "picard"
 - "clhsdb"
 - "hsdb"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
 - "appletviewer"
 - "idlj"
 - "orbd"
 - "schemagen"
 - "servertool"
 - "tnameserv"
 - "wsgen"
 - "wsimport"
 - "xjc"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "f2py3.7"
 - "jfr"
 - "2to3-3.7"
versions:
 - "1.0.0--pyhdfd78af_0"
 - "1.0.1--pyhdfd78af_0"
 - "1.0.1--pyhdfd78af_1"
description: "singularity registry hpc automated addition for geno2phenotb"
config: {"url": "https://biocontainers.pro/tools/geno2phenotb", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for geno2phenotb", "latest": {"1.0.1--pyhdfd78af_1": "sha256:835f6f7a3c7ec3360a6e6977e3033c683e0ffe9bdf5124a98c20b579575c8c83"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:43fe9d40dc675b423216b913be9de98740163efcc15525e6a6077d0d35bbbc1e", "1.0.1--pyhdfd78af_0": "sha256:cb0f94de875ebc002ffefda694952428898b13c0a384e7dd07d01bbec5a4bbd5", "1.0.1--pyhdfd78af_1": "sha256:835f6f7a3c7ec3360a6e6977e3033c683e0ffe9bdf5124a98c20b579575c8c83"}, "docker": "quay.io/biocontainers/geno2phenotb", "aliases": {"GenomeAnalysisTK": "/usr/local/bin/GenomeAnalysisTK", "MTBseq": "/usr/local/bin/MTBseq", "gatk3": "/usr/local/bin/gatk3", "geno2phenotb": "/usr/local/bin/geno2phenotb", "picard": "/usr/local/bin/picard", "clhsdb": "/usr/local/bin/clhsdb", "hsdb": "/usr/local/bin/hsdb", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd", "schemagen": "/usr/local/bin/schemagen", "servertool": "/usr/local/bin/servertool", "tnameserv": "/usr/local/bin/tnameserv", "wsgen": "/usr/local/bin/wsgen", "wsimport": "/usr/local/bin/wsimport", "xjc": "/usr/local/bin/xjc", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "f2py3.7": "/usr/local/bin/f2py3.7", "jfr": "/usr/local/bin/jfr", "2to3-3.7": "/usr/local/bin/2to3-3.7"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/geno2phenotb.
singularity registry hpc automated addition for geno2phenotb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/geno2phenotb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/geno2phenotb:1.0.1--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/geno2phenotb/1.0.1--pyhdfd78af_1
$ module help quay.io/biocontainers/geno2phenotb/1.0.1--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### geno2phenotb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### geno2phenotb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### geno2phenotb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### geno2phenotb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### geno2phenotb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### geno2phenotb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GenomeAnalysisTK

```bash
$ singularity exec <container> /usr/local/bin/GenomeAnalysisTK
$ podman run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MTBseq

```bash
$ singularity exec <container> /usr/local/bin/MTBseq
$ podman run --it --rm --entrypoint /usr/local/bin/MTBseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MTBseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk3

```bash
$ singularity exec <container> /usr/local/bin/gatk3
$ podman run --it --rm --entrypoint /usr/local/bin/gatk3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geno2phenotb

```bash
$ singularity exec <container> /usr/local/bin/geno2phenotb
$ podman run --it --rm --entrypoint /usr/local/bin/geno2phenotb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geno2phenotb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picard

```bash
$ singularity exec <container> /usr/local/bin/picard
$ podman run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clhsdb

```bash
$ singularity exec <container> /usr/local/bin/clhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsdb

```bash
$ singularity exec <container> /usr/local/bin/hsdb
$ podman run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhat

```bash
$ singularity exec <container> /usr/local/bin/jhat
$ podman run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsadebugd

```bash
$ singularity exec <container> /usr/local/bin/jsadebugd
$ podman run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### native2ascii

```bash
$ singularity exec <container> /usr/local/bin/native2ascii
$ podman run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### policytool

```bash
$ singularity exec <container> /usr/local/bin/policytool
$ podman run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idlj

```bash
$ singularity exec <container> /usr/local/bin/idlj
$ podman run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orbd

```bash
$ singularity exec <container> /usr/local/bin/orbd
$ podman run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### schemagen

```bash
$ singularity exec <container> /usr/local/bin/schemagen
$ podman run --it --rm --entrypoint /usr/local/bin/schemagen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/schemagen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### servertool

```bash
$ singularity exec <container> /usr/local/bin/servertool
$ podman run --it --rm --entrypoint /usr/local/bin/servertool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/servertool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tnameserv

```bash
$ singularity exec <container> /usr/local/bin/tnameserv
$ podman run --it --rm --entrypoint /usr/local/bin/tnameserv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tnameserv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsgen

```bash
$ singularity exec <container> /usr/local/bin/wsgen
$ podman run --it --rm --entrypoint /usr/local/bin/wsgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsimport

```bash
$ singularity exec <container> /usr/local/bin/wsimport
$ podman run --it --rm --entrypoint /usr/local/bin/wsimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xjc

```bash
$ singularity exec <container> /usr/local/bin/xjc
$ podman run --it --rm --entrypoint /usr/local/bin/xjc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xjc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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