---
layout: container
name:  "quay.io/biocontainers/perl-math-bigint"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-math-bigint/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-math-bigint/container.yaml"
updated_at: "2024-05-06 02:37:18.046363"
latest: "2.003002--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-math-bigint"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.999837--pl5321hdfd78af_0"
 - "1.999838--pl5321hdfd78af_0"
 - "1.999839--pl5321hdfd78af_0"
 - "1.999842--pl5321hdfd78af_0"
 - "1.999841--pl5321hdfd78af_0"
 - "2.001000--pl5321hdfd78af_0"
 - "2.000000--pl5321hdfd78af_0"
 - "2.002001--pl5321hdfd78af_0"
 - "2.002000--pl5321hdfd78af_0"
 - "2.001001--pl5321hdfd78af_0"
 - "2.003002--pl5321hdfd78af_0"
 - "2.003001--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-math-bigint"
config: {"url": "https://biocontainers.pro/tools/perl-math-bigint", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-math-bigint", "latest": {"2.003002--pl5321hdfd78af_0": "sha256:f57db80c8d9d9d5593f9a90fe07ed42ba87314e60e21b754c8b1027fe1ab9d87"}, "tags": {"1.999837--pl5321hdfd78af_0": "sha256:4868e5e1464818f7756a27ef93e27f84af8855e53e2a604beec4e35d8d4e5973", "1.999838--pl5321hdfd78af_0": "sha256:ad1b96d33f540f00081f7e520f7d3bc1382f9fcfef705697c1b0ff7668b67767", "1.999839--pl5321hdfd78af_0": "sha256:db31cc4dad65b78fdc2fab945750e298ea9528ff28bfd4d38aa6a29d8b3d4c42", "1.999842--pl5321hdfd78af_0": "sha256:64bf7116679d8d98ae20fe8b66f060060aeae3882b1534ab03d58738d299d990", "1.999841--pl5321hdfd78af_0": "sha256:00df165258ef204bec7c54dd53ae0147eb6028196cc078f71dc3ef13d9c3f326", "2.001000--pl5321hdfd78af_0": "sha256:cfd90ab60c56156519f284e7dda116e67db19dd5b74b57f240cfd796858077b9", "2.000000--pl5321hdfd78af_0": "sha256:ea96c8a5efb2bbacbd1133dce81b5f5cb40d272cdfcb5b214f5b291b7b7cf18d", "2.002001--pl5321hdfd78af_0": "sha256:3edee6d0cfe316b5c415c7e8ccd3498bca9db6cb9a2ce1a4e783c381c0d90e03", "2.002000--pl5321hdfd78af_0": "sha256:763438b274750df72efeb9a7f3ace9bca74095d18d9c946a1332748c49376cc4", "2.001001--pl5321hdfd78af_0": "sha256:172bfb0c844cecfc6fce798d4eced9b851a5b34f56ff433a1ec1d96f61b8db5e", "2.003002--pl5321hdfd78af_0": "sha256:f57db80c8d9d9d5593f9a90fe07ed42ba87314e60e21b754c8b1027fe1ab9d87", "2.003001--pl5321hdfd78af_0": "sha256:bfa522207accedff0b9b2bb0aa15b984530ef24ee50dbf2e898d8460577e77d2"}, "docker": "quay.io/biocontainers/perl-math-bigint", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-math-bigint.
shpc-registry automated BioContainers addition for perl-math-bigint
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-math-bigint
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-math-bigint:2.003002--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-math-bigint/2.003002--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-math-bigint/2.003002--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-math-bigint-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-math-bigint-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-math-bigint-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-math-bigint-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-math-bigint-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-math-bigint-inspect-deffile:

```bash
$ singularity inspect -d <container>
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