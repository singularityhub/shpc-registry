---
layout: container
name:  "quay.io/biocontainers/fragpipe-speclib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fragpipe-speclib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fragpipe-speclib/container.yaml"
updated_at: "2026-10-26 00:26:43.584108"
latest: "0.1.59--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/fragpipe-speclib"
aliases:
 - "fragpipe-speclib"
 - "svm-predict"
 - "svm-scale"
 - "svm-train"
 - "pax11publish"
 - "CreateDOMDocument"
 - "DOMCount"
 - "DOMPrint"
 - "EnumVal"
 - "MemParse"
 - "PParse"
 - "PSVIWriter"
 - "Redirect"
 - "SAX2Count"
 - "SAX2Print"
 - "SAXCount"
 - "SAXPrint"
 - "SCMPrint"
 - "SEnumVal"
 - "StdInParse"
 - "XInclude"
 - "ldapadd"
 - "ldapcompare"
 - "ldapdelete"
 - "ldapexop"
 - "ldapmodify"
versions:
 - "0.1.59--pyh106432d_0"
description: "singularity registry hpc automated addition for fragpipe-speclib"
config: {"url": "https://biocontainers.pro/tools/fragpipe-speclib", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fragpipe-speclib", "latest": {"0.1.59--pyh106432d_0": "sha256:55dc45e15ccc9e2171c62d8e61a8651ee8afa354464f19c6ed98676761e44bbe"}, "tags": {"0.1.59--pyh106432d_0": "sha256:55dc45e15ccc9e2171c62d8e61a8651ee8afa354464f19c6ed98676761e44bbe"}, "docker": "quay.io/biocontainers/fragpipe-speclib", "aliases": {"fragpipe-speclib": "/usr/local/bin/fragpipe-speclib", "svm-predict": "/usr/local/bin/svm-predict", "svm-scale": "/usr/local/bin/svm-scale", "svm-train": "/usr/local/bin/svm-train", "pax11publish": "/usr/local/bin/pax11publish", "CreateDOMDocument": "/usr/local/bin/CreateDOMDocument", "DOMCount": "/usr/local/bin/DOMCount", "DOMPrint": "/usr/local/bin/DOMPrint", "EnumVal": "/usr/local/bin/EnumVal", "MemParse": "/usr/local/bin/MemParse", "PParse": "/usr/local/bin/PParse", "PSVIWriter": "/usr/local/bin/PSVIWriter", "Redirect": "/usr/local/bin/Redirect", "SAX2Count": "/usr/local/bin/SAX2Count", "SAX2Print": "/usr/local/bin/SAX2Print", "SAXCount": "/usr/local/bin/SAXCount", "SAXPrint": "/usr/local/bin/SAXPrint", "SCMPrint": "/usr/local/bin/SCMPrint", "SEnumVal": "/usr/local/bin/SEnumVal", "StdInParse": "/usr/local/bin/StdInParse", "XInclude": "/usr/local/bin/XInclude", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fragpipe-speclib.
singularity registry hpc automated addition for fragpipe-speclib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fragpipe-speclib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fragpipe-speclib:0.1.59--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fragpipe-speclib/0.1.59--pyh106432d_0
$ module help quay.io/biocontainers/fragpipe-speclib/0.1.59--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fragpipe-speclib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fragpipe-speclib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fragpipe-speclib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fragpipe-speclib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fragpipe-speclib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fragpipe-speclib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fragpipe-speclib

```bash
$ singularity exec <container> /usr/local/bin/fragpipe-speclib
$ podman run --it --rm --entrypoint /usr/local/bin/fragpipe-speclib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragpipe-speclib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-predict

```bash
$ singularity exec <container> /usr/local/bin/svm-predict
$ podman run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-scale

```bash
$ singularity exec <container> /usr/local/bin/svm-scale
$ podman run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-train

```bash
$ singularity exec <container> /usr/local/bin/svm-train
$ podman run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pax11publish

```bash
$ singularity exec <container> /usr/local/bin/pax11publish
$ podman run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CreateDOMDocument

```bash
$ singularity exec <container> /usr/local/bin/CreateDOMDocument
$ podman run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMCount

```bash
$ singularity exec <container> /usr/local/bin/DOMCount
$ podman run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMPrint

```bash
$ singularity exec <container> /usr/local/bin/DOMPrint
$ podman run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnumVal

```bash
$ singularity exec <container> /usr/local/bin/EnumVal
$ podman run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MemParse

```bash
$ singularity exec <container> /usr/local/bin/MemParse
$ podman run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PParse

```bash
$ singularity exec <container> /usr/local/bin/PParse
$ podman run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PSVIWriter

```bash
$ singularity exec <container> /usr/local/bin/PSVIWriter
$ podman run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Redirect

```bash
$ singularity exec <container> /usr/local/bin/Redirect
$ podman run --it --rm --entrypoint /usr/local/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Count

```bash
$ singularity exec <container> /usr/local/bin/SAX2Count
$ podman run --it --rm --entrypoint /usr/local/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Print

```bash
$ singularity exec <container> /usr/local/bin/SAX2Print
$ podman run --it --rm --entrypoint /usr/local/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAXCount

```bash
$ singularity exec <container> /usr/local/bin/SAXCount
$ podman run --it --rm --entrypoint /usr/local/bin/SAXCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAXCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAXPrint

```bash
$ singularity exec <container> /usr/local/bin/SAXPrint
$ podman run --it --rm --entrypoint /usr/local/bin/SAXPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAXPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SCMPrint

```bash
$ singularity exec <container> /usr/local/bin/SCMPrint
$ podman run --it --rm --entrypoint /usr/local/bin/SCMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SCMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SEnumVal

```bash
$ singularity exec <container> /usr/local/bin/SEnumVal
$ podman run --it --rm --entrypoint /usr/local/bin/SEnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SEnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StdInParse

```bash
$ singularity exec <container> /usr/local/bin/StdInParse
$ podman run --it --rm --entrypoint /usr/local/bin/StdInParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StdInParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### XInclude

```bash
$ singularity exec <container> /usr/local/bin/XInclude
$ podman run --it --rm --entrypoint /usr/local/bin/XInclude   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/XInclude   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapadd

```bash
$ singularity exec <container> /usr/local/bin/ldapadd
$ podman run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapcompare

```bash
$ singularity exec <container> /usr/local/bin/ldapcompare
$ podman run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapdelete

```bash
$ singularity exec <container> /usr/local/bin/ldapdelete
$ podman run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapexop

```bash
$ singularity exec <container> /usr/local/bin/ldapexop
$ podman run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodify

```bash
$ singularity exec <container> /usr/local/bin/ldapmodify
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
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