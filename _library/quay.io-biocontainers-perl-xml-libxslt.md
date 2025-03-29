---
layout: container
name:  "quay.io/biocontainers/perl-xml-libxslt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-xml-libxslt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-xml-libxslt/container.yaml"
updated_at: "2025-03-29 03:34:19.551169"
latest: "2.003000--pl5321h7b50bb2_2"
container_url: "https://biocontainers.pro/tools/perl-xml-libxslt"
aliases:
 - "xml2-config.bak"
 - "xslt-config"
 - "xsltproc"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.002000--pl5321hec16e2b_1"
 - "2.002001--pl5321hec16e2b_0"
 - "2.002001--pl5321h031d066_2"
 - "2.003000--pl5321h031d066_0"
 - "2.003000--pl5321h7b50bb2_1"
 - "2.003000--pl5321h7b50bb2_2"
description: "shpc-registry automated BioContainers addition for perl-xml-libxslt"
config: {"url": "https://biocontainers.pro/tools/perl-xml-libxslt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-xml-libxslt", "latest": {"2.003000--pl5321h7b50bb2_2": "sha256:a91bd003527c9560c1e4c6a9f0a48d2a462845697a66f42f67366d2c0614a887"}, "tags": {"2.002000--pl5321hec16e2b_1": "sha256:d6537980923761e3987021808ce0f0b8a44cdfbd49da8d68d99c345697faaf79", "2.002001--pl5321hec16e2b_0": "sha256:809ce70dc82ab6251878c5d3568d7fb394df721b0c9176cfd420ccb1a5c54cc9", "2.002001--pl5321h031d066_2": "sha256:19a0e2c1701a248675b3b9a73ee365a82128f09a23cfcc321f9af96d7fbdf118", "2.003000--pl5321h031d066_0": "sha256:b51489ba3080b1df30ad7607d2b84a16b089a5636cbb36b4cfc2430706fabf5a", "2.003000--pl5321h7b50bb2_1": "sha256:f635e7cc045a5e3325b98c71bc8ce393ee52fd5ce23ae8732acfc44a0849f931", "2.003000--pl5321h7b50bb2_2": "sha256:a91bd003527c9560c1e4c6a9f0a48d2a462845697a66f42f67366d2c0614a887"}, "docker": "quay.io/biocontainers/perl-xml-libxslt", "aliases": {"xml2-config.bak": "/usr/local/bin/xml2-config.bak", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-xml-libxslt.
shpc-registry automated BioContainers addition for perl-xml-libxslt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-xml-libxslt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-xml-libxslt:2.003000--pl5321h7b50bb2_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-xml-libxslt/2.003000--pl5321h7b50bb2_2
$ module help quay.io/biocontainers/perl-xml-libxslt/2.003000--pl5321h7b50bb2_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-xml-libxslt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-xml-libxslt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-xml-libxslt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-xml-libxslt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-xml-libxslt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-xml-libxslt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xml2-config.bak

```bash
$ singularity exec <container> /usr/local/bin/xml2-config.bak
$ podman run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
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