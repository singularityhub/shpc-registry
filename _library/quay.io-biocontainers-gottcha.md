---
layout: container
name:  "quay.io/biocontainers/gottcha"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gottcha/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gottcha/container.yaml"
updated_at: "2023-01-31 03:31:50.084962"
latest: "1.0--pl526_2"
container_url: "https://biocontainers.pro/tools/gottcha"
aliases:
 - "convert_abu2list.pl"
 - "filterGottcha.pl"
 - "gottcha.pl"
 - "gottcha_db.pl"
 - "makeVariantTaxLookups.pl"
 - "mkGottchaTaxTree.pl"
 - "mkGottchaXML.pl"
 - "profileGottcha.pl"
 - "splitrim"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "perl5.26.2"
 - "podselect"
versions:
 - "1.0--pl526_2"
description: "shpc-registry automated BioContainers addition for gottcha"
config: {"url": "https://biocontainers.pro/tools/gottcha", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gottcha", "latest": {"1.0--pl526_2": "sha256:1fab9581afbc7cb8765364707bb583796ca2436e36355d5b914cab555b6b0c15"}, "tags": {"1.0--pl526_2": "sha256:1fab9581afbc7cb8765364707bb583796ca2436e36355d5b914cab555b6b0c15"}, "docker": "quay.io/biocontainers/gottcha", "aliases": {"convert_abu2list.pl": "/usr/local/bin/convert_abu2list.pl", "filterGottcha.pl": "/usr/local/bin/filterGottcha.pl", "gottcha.pl": "/usr/local/bin/gottcha.pl", "gottcha_db.pl": "/usr/local/bin/gottcha_db.pl", "makeVariantTaxLookups.pl": "/usr/local/bin/makeVariantTaxLookups.pl", "mkGottchaTaxTree.pl": "/usr/local/bin/mkGottchaTaxTree.pl", "mkGottchaXML.pl": "/usr/local/bin/mkGottchaXML.pl", "profileGottcha.pl": "/usr/local/bin/profileGottcha.pl", "splitrim": "/usr/local/bin/splitrim", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gottcha.
shpc-registry automated BioContainers addition for gottcha
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gottcha
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gottcha:1.0--pl526_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gottcha/1.0--pl526_2
$ module help quay.io/biocontainers/gottcha/1.0--pl526_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gottcha-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gottcha-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gottcha-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gottcha-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gottcha-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gottcha-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convert_abu2list.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_abu2list.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_abu2list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_abu2list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterGottcha.pl

```bash
$ singularity exec <container> /usr/local/bin/filterGottcha.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filterGottcha.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterGottcha.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gottcha.pl

```bash
$ singularity exec <container> /usr/local/bin/gottcha.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gottcha.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gottcha.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gottcha_db.pl

```bash
$ singularity exec <container> /usr/local/bin/gottcha_db.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gottcha_db.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gottcha_db.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeVariantTaxLookups.pl

```bash
$ singularity exec <container> /usr/local/bin/makeVariantTaxLookups.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makeVariantTaxLookups.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeVariantTaxLookups.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkGottchaTaxTree.pl

```bash
$ singularity exec <container> /usr/local/bin/mkGottchaTaxTree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mkGottchaTaxTree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkGottchaTaxTree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkGottchaXML.pl

```bash
$ singularity exec <container> /usr/local/bin/mkGottchaXML.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mkGottchaXML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkGottchaXML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### profileGottcha.pl

```bash
$ singularity exec <container> /usr/local/bin/profileGottcha.pl
$ podman run --it --rm --entrypoint /usr/local/bin/profileGottcha.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/profileGottcha.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitrim

```bash
$ singularity exec <container> /usr/local/bin/splitrim
$ podman run --it --rm --entrypoint /usr/local/bin/splitrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitrim   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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