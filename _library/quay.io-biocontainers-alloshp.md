---
layout: container
name:  "quay.io/biocontainers/alloshp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alloshp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/alloshp/container.yaml"
updated_at: "2025-09-25 03:09:43.615710"
latest: "2025.09.08d--h7b50bb2_0"
container_url: "https://biocontainers.pro/tools/alloshp"
aliases:
 - "GSAlign"
 - "Red"
 - "WGA"
 - "WGA.bak"
 - "bwt_index"
 - "vcf2alignment"
 - "vcf2synteny"
 - "version.txt"
 - "zless"
 - "pax11publish"
 - "ldapadd"
 - "ldapcompare"
 - "ldapdelete"
 - "ldapexop"
 - "ldapmodify"
 - "ldapmodrdn"
 - "ldappasswd"
 - "ldapsearch"
 - "ldapurl"
 - "ldapvc"
 - "ldapwhoami"
 - "gunzip"
 - "gzexe"
 - "gzip"
 - "uncompress"
 - "zcat"
 - "zcmp"
 - "zdiff"
 - "zegrep"
 - "zfgrep"
 - "zforce"
 - "zgrep"
 - "zmore"
 - "znew"
versions:
 - "2025.09.08d--h7b50bb2_0"
description: "singularity registry hpc automated addition for alloshp"
config: {"url": "https://biocontainers.pro/tools/alloshp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for alloshp", "latest": {"2025.09.08d--h7b50bb2_0": "sha256:736f6f09bb5322ffe1e73664f2eae56a2036aa5d484d890e9ebf3b208093307b"}, "tags": {"2025.09.08d--h7b50bb2_0": "sha256:736f6f09bb5322ffe1e73664f2eae56a2036aa5d484d890e9ebf3b208093307b"}, "docker": "quay.io/biocontainers/alloshp", "aliases": {"GSAlign": "/usr/local/bin/GSAlign", "Red": "/usr/local/bin/Red", "WGA": "/usr/local/bin/WGA", "WGA.bak": "/usr/local/bin/WGA.bak", "bwt_index": "/usr/local/bin/bwt_index", "vcf2alignment": "/usr/local/bin/vcf2alignment", "vcf2synteny": "/usr/local/bin/vcf2synteny", "version.txt": "/usr/local/bin/version.txt", "zless": "/usr/local/bin/zless", "pax11publish": "/usr/local/bin/pax11publish", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify", "ldapmodrdn": "/usr/local/bin/ldapmodrdn", "ldappasswd": "/usr/local/bin/ldappasswd", "ldapsearch": "/usr/local/bin/ldapsearch", "ldapurl": "/usr/local/bin/ldapurl", "ldapvc": "/usr/local/bin/ldapvc", "ldapwhoami": "/usr/local/bin/ldapwhoami", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alloshp.
singularity registry hpc automated addition for alloshp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alloshp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alloshp:2025.09.08d--h7b50bb2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alloshp/2025.09.08d--h7b50bb2_0
$ module help quay.io/biocontainers/alloshp/2025.09.08d--h7b50bb2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alloshp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alloshp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alloshp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alloshp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alloshp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alloshp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GSAlign

```bash
$ singularity exec <container> /usr/local/bin/GSAlign
$ podman run --it --rm --entrypoint /usr/local/bin/GSAlign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GSAlign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Red

```bash
$ singularity exec <container> /usr/local/bin/Red
$ podman run --it --rm --entrypoint /usr/local/bin/Red   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Red   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### WGA

```bash
$ singularity exec <container> /usr/local/bin/WGA
$ podman run --it --rm --entrypoint /usr/local/bin/WGA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WGA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### WGA.bak

```bash
$ singularity exec <container> /usr/local/bin/WGA.bak
$ podman run --it --rm --entrypoint /usr/local/bin/WGA.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WGA.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwt_index

```bash
$ singularity exec <container> /usr/local/bin/bwt_index
$ podman run --it --rm --entrypoint /usr/local/bin/bwt_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwt_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2alignment

```bash
$ singularity exec <container> /usr/local/bin/vcf2alignment
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2synteny

```bash
$ singularity exec <container> /usr/local/bin/vcf2synteny
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2synteny   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2synteny   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### version.txt

```bash
$ singularity exec <container> /usr/local/bin/version.txt
$ podman run --it --rm --entrypoint /usr/local/bin/version.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/version.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zless

```bash
$ singularity exec <container> /usr/local/bin/zless
$ podman run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pax11publish

```bash
$ singularity exec <container> /usr/local/bin/pax11publish
$ podman run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ldapmodrdn

```bash
$ singularity exec <container> /usr/local/bin/ldapmodrdn
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldappasswd

```bash
$ singularity exec <container> /usr/local/bin/ldappasswd
$ podman run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapsearch

```bash
$ singularity exec <container> /usr/local/bin/ldapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapurl

```bash
$ singularity exec <container> /usr/local/bin/ldapurl
$ podman run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapvc

```bash
$ singularity exec <container> /usr/local/bin/ldapvc
$ podman run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapwhoami

```bash
$ singularity exec <container> /usr/local/bin/ldapwhoami
$ podman run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gunzip

```bash
$ singularity exec <container> /usr/local/bin/gunzip
$ podman run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzexe

```bash
$ singularity exec <container> /usr/local/bin/gzexe
$ podman run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzip

```bash
$ singularity exec <container> /usr/local/bin/gzip
$ podman run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uncompress

```bash
$ singularity exec <container> /usr/local/bin/uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcat

```bash
$ singularity exec <container> /usr/local/bin/zcat
$ podman run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcmp

```bash
$ singularity exec <container> /usr/local/bin/zcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zdiff

```bash
$ singularity exec <container> /usr/local/bin/zdiff
$ podman run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zegrep

```bash
$ singularity exec <container> /usr/local/bin/zegrep
$ podman run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfgrep

```bash
$ singularity exec <container> /usr/local/bin/zfgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zforce

```bash
$ singularity exec <container> /usr/local/bin/zforce
$ podman run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zgrep

```bash
$ singularity exec <container> /usr/local/bin/zgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmore

```bash
$ singularity exec <container> /usr/local/bin/zmore
$ podman run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### znew

```bash
$ singularity exec <container> /usr/local/bin/znew
$ podman run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
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