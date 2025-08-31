---
layout: container
name:  "quay.io/biocontainers/r-pspecterlib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-pspecterlib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-pspecterlib/container.yaml"
updated_at: "2025-08-31 03:15:29.616887"
latest: "1.1.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-pspecterlib"
aliases:
 - "aprofutil"
 - "mono-hang-watchdog"
 - "csc"
 - "csi"
 - "illinkanalyzer"
 - "vbc"
 - "mono-package-runtime"
 - "sgen-grep-binprot"
 - "al"
 - "al2"
 - "caspol"
 - "cccheck"
 - "ccrewrite"
 - "cert-sync"
 - "cert2spc"
 - "certmgr"
 - "chktrust"
 - "crlupdate"
 - "csharp"
 - "dmcs"
 - "dtd2rng"
 - "dtd2xsd"
 - "gacutil"
 - "gacutil2"
 - "genxs"
 - "httpcfg"
 - "ikdasm"
versions:
 - "1.1.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for r-pspecterlib"
config: {"url": "https://biocontainers.pro/tools/r-pspecterlib", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-pspecterlib", "latest": {"1.1.0--r43hdfd78af_0": "sha256:52faf5bdee53d70cc4e63a6b9efb0ff01635e87e9945de40807a36aabc5d43d6"}, "tags": {"1.1.0--r43hdfd78af_0": "sha256:52faf5bdee53d70cc4e63a6b9efb0ff01635e87e9945de40807a36aabc5d43d6"}, "docker": "quay.io/biocontainers/r-pspecterlib", "aliases": {"aprofutil": "/usr/local/bin/aprofutil", "mono-hang-watchdog": "/usr/local/bin/mono-hang-watchdog", "csc": "/usr/local/bin/csc", "csi": "/usr/local/bin/csi", "illinkanalyzer": "/usr/local/bin/illinkanalyzer", "vbc": "/usr/local/bin/vbc", "mono-package-runtime": "/usr/local/bin/mono-package-runtime", "sgen-grep-binprot": "/usr/local/bin/sgen-grep-binprot", "al": "/usr/local/bin/al", "al2": "/usr/local/bin/al2", "caspol": "/usr/local/bin/caspol", "cccheck": "/usr/local/bin/cccheck", "ccrewrite": "/usr/local/bin/ccrewrite", "cert-sync": "/usr/local/bin/cert-sync", "cert2spc": "/usr/local/bin/cert2spc", "certmgr": "/usr/local/bin/certmgr", "chktrust": "/usr/local/bin/chktrust", "crlupdate": "/usr/local/bin/crlupdate", "csharp": "/usr/local/bin/csharp", "dmcs": "/usr/local/bin/dmcs", "dtd2rng": "/usr/local/bin/dtd2rng", "dtd2xsd": "/usr/local/bin/dtd2xsd", "gacutil": "/usr/local/bin/gacutil", "gacutil2": "/usr/local/bin/gacutil2", "genxs": "/usr/local/bin/genxs", "httpcfg": "/usr/local/bin/httpcfg", "ikdasm": "/usr/local/bin/ikdasm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-pspecterlib.
singularity registry hpc automated addition for r-pspecterlib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-pspecterlib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-pspecterlib:1.1.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-pspecterlib/1.1.0--r43hdfd78af_0
$ module help quay.io/biocontainers/r-pspecterlib/1.1.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-pspecterlib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-pspecterlib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-pspecterlib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-pspecterlib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-pspecterlib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-pspecterlib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aprofutil

```bash
$ singularity exec <container> /usr/local/bin/aprofutil
$ podman run --it --rm --entrypoint /usr/local/bin/aprofutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aprofutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-hang-watchdog

```bash
$ singularity exec <container> /usr/local/bin/mono-hang-watchdog
$ podman run --it --rm --entrypoint /usr/local/bin/mono-hang-watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-hang-watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csc

```bash
$ singularity exec <container> /usr/local/bin/csc
$ podman run --it --rm --entrypoint /usr/local/bin/csc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csi

```bash
$ singularity exec <container> /usr/local/bin/csi
$ podman run --it --rm --entrypoint /usr/local/bin/csi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### illinkanalyzer

```bash
$ singularity exec <container> /usr/local/bin/illinkanalyzer
$ podman run --it --rm --entrypoint /usr/local/bin/illinkanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/illinkanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vbc

```bash
$ singularity exec <container> /usr/local/bin/vbc
$ podman run --it --rm --entrypoint /usr/local/bin/vbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-package-runtime

```bash
$ singularity exec <container> /usr/local/bin/mono-package-runtime
$ podman run --it --rm --entrypoint /usr/local/bin/mono-package-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-package-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sgen-grep-binprot

```bash
$ singularity exec <container> /usr/local/bin/sgen-grep-binprot
$ podman run --it --rm --entrypoint /usr/local/bin/sgen-grep-binprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sgen-grep-binprot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### al

```bash
$ singularity exec <container> /usr/local/bin/al
$ podman run --it --rm --entrypoint /usr/local/bin/al   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/al   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### al2

```bash
$ singularity exec <container> /usr/local/bin/al2
$ podman run --it --rm --entrypoint /usr/local/bin/al2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/al2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### caspol

```bash
$ singularity exec <container> /usr/local/bin/caspol
$ podman run --it --rm --entrypoint /usr/local/bin/caspol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/caspol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cccheck

```bash
$ singularity exec <container> /usr/local/bin/cccheck
$ podman run --it --rm --entrypoint /usr/local/bin/cccheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cccheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccrewrite

```bash
$ singularity exec <container> /usr/local/bin/ccrewrite
$ podman run --it --rm --entrypoint /usr/local/bin/ccrewrite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccrewrite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cert-sync

```bash
$ singularity exec <container> /usr/local/bin/cert-sync
$ podman run --it --rm --entrypoint /usr/local/bin/cert-sync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cert-sync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cert2spc

```bash
$ singularity exec <container> /usr/local/bin/cert2spc
$ podman run --it --rm --entrypoint /usr/local/bin/cert2spc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cert2spc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certmgr

```bash
$ singularity exec <container> /usr/local/bin/certmgr
$ podman run --it --rm --entrypoint /usr/local/bin/certmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chktrust

```bash
$ singularity exec <container> /usr/local/bin/chktrust
$ podman run --it --rm --entrypoint /usr/local/bin/chktrust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chktrust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crlupdate

```bash
$ singularity exec <container> /usr/local/bin/crlupdate
$ podman run --it --rm --entrypoint /usr/local/bin/crlupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crlupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csharp

```bash
$ singularity exec <container> /usr/local/bin/csharp
$ podman run --it --rm --entrypoint /usr/local/bin/csharp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csharp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmcs

```bash
$ singularity exec <container> /usr/local/bin/dmcs
$ podman run --it --rm --entrypoint /usr/local/bin/dmcs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmcs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dtd2rng

```bash
$ singularity exec <container> /usr/local/bin/dtd2rng
$ podman run --it --rm --entrypoint /usr/local/bin/dtd2rng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtd2rng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dtd2xsd

```bash
$ singularity exec <container> /usr/local/bin/dtd2xsd
$ podman run --it --rm --entrypoint /usr/local/bin/dtd2xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtd2xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gacutil

```bash
$ singularity exec <container> /usr/local/bin/gacutil
$ podman run --it --rm --entrypoint /usr/local/bin/gacutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gacutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gacutil2

```bash
$ singularity exec <container> /usr/local/bin/gacutil2
$ podman run --it --rm --entrypoint /usr/local/bin/gacutil2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gacutil2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genxs

```bash
$ singularity exec <container> /usr/local/bin/genxs
$ podman run --it --rm --entrypoint /usr/local/bin/genxs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genxs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpcfg

```bash
$ singularity exec <container> /usr/local/bin/httpcfg
$ podman run --it --rm --entrypoint /usr/local/bin/httpcfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpcfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ikdasm

```bash
$ singularity exec <container> /usr/local/bin/ikdasm
$ podman run --it --rm --entrypoint /usr/local/bin/ikdasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ikdasm   -v ${PWD} -w ${PWD} <container> -c " $@"
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