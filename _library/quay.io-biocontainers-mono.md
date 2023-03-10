---
layout: container
name:  "quay.io/biocontainers/mono"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mono/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mono/container.yaml"
updated_at: "2023-03-10 03:20:54.676289"
latest: "4.6.2.6--0"
container_url: "https://biocontainers.pro/tools/mono"
aliases:
 - "mono"
 - "mono-api-html"
 - "mono-api-info"
 - "mono-boehm"
 - "mono-cil-strip"
 - "mono-configuration-crypto"
 - "mono-find-provides"
 - "mono-find-requires"
 - "mono-gdb.py"
 - "mono-heapviz"
 - "mono-service"
 - "mono-service2"
 - "mono-sgen"
 - "mono-sgen-gdb.py"
 - "mono-shlib-cop"
 - "mono-symbolicate"
 - "mono-test-install"
 - "mono-xmltool"
 - "monodis"
 - "monodocer"
 - "monodocs2html"
 - "monodocs2slashdoc"
 - "monolinker"
 - "monop"
 - "monop2"
 - "nunit-console"
 - "nunit-console2"
 - "nunit-console4"
 - "prj2make"
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
versions:
 - "4.6.2.6--0"
description: "shpc-registry automated BioContainers addition for mono"
config: {"url": "https://biocontainers.pro/tools/mono", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mono", "latest": {"4.6.2.6--0": "sha256:23f820b58776a14ef6fdb1f1d21eb9353757b09574860f6ec758ce482e514c9a"}, "tags": {"4.6.2.6--0": "sha256:23f820b58776a14ef6fdb1f1d21eb9353757b09574860f6ec758ce482e514c9a"}, "docker": "quay.io/biocontainers/mono", "aliases": {"mono": "/usr/local/bin/mono", "mono-api-html": "/usr/local/bin/mono-api-html", "mono-api-info": "/usr/local/bin/mono-api-info", "mono-boehm": "/usr/local/bin/mono-boehm", "mono-cil-strip": "/usr/local/bin/mono-cil-strip", "mono-configuration-crypto": "/usr/local/bin/mono-configuration-crypto", "mono-find-provides": "/usr/local/bin/mono-find-provides", "mono-find-requires": "/usr/local/bin/mono-find-requires", "mono-gdb.py": "/usr/local/bin/mono-gdb.py", "mono-heapviz": "/usr/local/bin/mono-heapviz", "mono-service": "/usr/local/bin/mono-service", "mono-service2": "/usr/local/bin/mono-service2", "mono-sgen": "/usr/local/bin/mono-sgen", "mono-sgen-gdb.py": "/usr/local/bin/mono-sgen-gdb.py", "mono-shlib-cop": "/usr/local/bin/mono-shlib-cop", "mono-symbolicate": "/usr/local/bin/mono-symbolicate", "mono-test-install": "/usr/local/bin/mono-test-install", "mono-xmltool": "/usr/local/bin/mono-xmltool", "monodis": "/usr/local/bin/monodis", "monodocer": "/usr/local/bin/monodocer", "monodocs2html": "/usr/local/bin/monodocs2html", "monodocs2slashdoc": "/usr/local/bin/monodocs2slashdoc", "monolinker": "/usr/local/bin/monolinker", "monop": "/usr/local/bin/monop", "monop2": "/usr/local/bin/monop2", "nunit-console": "/usr/local/bin/nunit-console", "nunit-console2": "/usr/local/bin/nunit-console2", "nunit-console4": "/usr/local/bin/nunit-console4", "prj2make": "/usr/local/bin/prj2make", "al": "/usr/local/bin/al", "al2": "/usr/local/bin/al2", "caspol": "/usr/local/bin/caspol", "cccheck": "/usr/local/bin/cccheck", "ccrewrite": "/usr/local/bin/ccrewrite", "cert-sync": "/usr/local/bin/cert-sync", "cert2spc": "/usr/local/bin/cert2spc", "certmgr": "/usr/local/bin/certmgr", "chktrust": "/usr/local/bin/chktrust", "crlupdate": "/usr/local/bin/crlupdate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mono.
shpc-registry automated BioContainers addition for mono
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mono
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mono:4.6.2.6--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mono/4.6.2.6--0
$ module help quay.io/biocontainers/mono/4.6.2.6--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mono-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mono-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mono-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mono-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mono-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mono-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mono

```bash
$ singularity exec <container> /usr/local/bin/mono
$ podman run --it --rm --entrypoint /usr/local/bin/mono   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-api-html

```bash
$ singularity exec <container> /usr/local/bin/mono-api-html
$ podman run --it --rm --entrypoint /usr/local/bin/mono-api-html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-api-html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-api-info

```bash
$ singularity exec <container> /usr/local/bin/mono-api-info
$ podman run --it --rm --entrypoint /usr/local/bin/mono-api-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-api-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-boehm

```bash
$ singularity exec <container> /usr/local/bin/mono-boehm
$ podman run --it --rm --entrypoint /usr/local/bin/mono-boehm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-boehm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-cil-strip

```bash
$ singularity exec <container> /usr/local/bin/mono-cil-strip
$ podman run --it --rm --entrypoint /usr/local/bin/mono-cil-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-cil-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-configuration-crypto

```bash
$ singularity exec <container> /usr/local/bin/mono-configuration-crypto
$ podman run --it --rm --entrypoint /usr/local/bin/mono-configuration-crypto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-configuration-crypto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-find-provides

```bash
$ singularity exec <container> /usr/local/bin/mono-find-provides
$ podman run --it --rm --entrypoint /usr/local/bin/mono-find-provides   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-find-provides   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-find-requires

```bash
$ singularity exec <container> /usr/local/bin/mono-find-requires
$ podman run --it --rm --entrypoint /usr/local/bin/mono-find-requires   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-find-requires   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-gdb.py

```bash
$ singularity exec <container> /usr/local/bin/mono-gdb.py
$ podman run --it --rm --entrypoint /usr/local/bin/mono-gdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-gdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-heapviz

```bash
$ singularity exec <container> /usr/local/bin/mono-heapviz
$ podman run --it --rm --entrypoint /usr/local/bin/mono-heapviz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-heapviz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-service

```bash
$ singularity exec <container> /usr/local/bin/mono-service
$ podman run --it --rm --entrypoint /usr/local/bin/mono-service   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-service   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-service2

```bash
$ singularity exec <container> /usr/local/bin/mono-service2
$ podman run --it --rm --entrypoint /usr/local/bin/mono-service2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-service2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-sgen

```bash
$ singularity exec <container> /usr/local/bin/mono-sgen
$ podman run --it --rm --entrypoint /usr/local/bin/mono-sgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-sgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-sgen-gdb.py

```bash
$ singularity exec <container> /usr/local/bin/mono-sgen-gdb.py
$ podman run --it --rm --entrypoint /usr/local/bin/mono-sgen-gdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-sgen-gdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-shlib-cop

```bash
$ singularity exec <container> /usr/local/bin/mono-shlib-cop
$ podman run --it --rm --entrypoint /usr/local/bin/mono-shlib-cop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-shlib-cop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-symbolicate

```bash
$ singularity exec <container> /usr/local/bin/mono-symbolicate
$ podman run --it --rm --entrypoint /usr/local/bin/mono-symbolicate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-symbolicate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-test-install

```bash
$ singularity exec <container> /usr/local/bin/mono-test-install
$ podman run --it --rm --entrypoint /usr/local/bin/mono-test-install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-test-install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-xmltool

```bash
$ singularity exec <container> /usr/local/bin/mono-xmltool
$ podman run --it --rm --entrypoint /usr/local/bin/mono-xmltool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-xmltool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monodis

```bash
$ singularity exec <container> /usr/local/bin/monodis
$ podman run --it --rm --entrypoint /usr/local/bin/monodis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monodis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monodocer

```bash
$ singularity exec <container> /usr/local/bin/monodocer
$ podman run --it --rm --entrypoint /usr/local/bin/monodocer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monodocer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monodocs2html

```bash
$ singularity exec <container> /usr/local/bin/monodocs2html
$ podman run --it --rm --entrypoint /usr/local/bin/monodocs2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monodocs2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monodocs2slashdoc

```bash
$ singularity exec <container> /usr/local/bin/monodocs2slashdoc
$ podman run --it --rm --entrypoint /usr/local/bin/monodocs2slashdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monodocs2slashdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monolinker

```bash
$ singularity exec <container> /usr/local/bin/monolinker
$ podman run --it --rm --entrypoint /usr/local/bin/monolinker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monolinker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monop

```bash
$ singularity exec <container> /usr/local/bin/monop
$ podman run --it --rm --entrypoint /usr/local/bin/monop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monop2

```bash
$ singularity exec <container> /usr/local/bin/monop2
$ podman run --it --rm --entrypoint /usr/local/bin/monop2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monop2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nunit-console

```bash
$ singularity exec <container> /usr/local/bin/nunit-console
$ podman run --it --rm --entrypoint /usr/local/bin/nunit-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nunit-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nunit-console2

```bash
$ singularity exec <container> /usr/local/bin/nunit-console2
$ podman run --it --rm --entrypoint /usr/local/bin/nunit-console2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nunit-console2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nunit-console4

```bash
$ singularity exec <container> /usr/local/bin/nunit-console4
$ podman run --it --rm --entrypoint /usr/local/bin/nunit-console4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nunit-console4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prj2make

```bash
$ singularity exec <container> /usr/local/bin/prj2make
$ podman run --it --rm --entrypoint /usr/local/bin/prj2make   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prj2make   -v ${PWD} -w ${PWD} <container> -c " $@"
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