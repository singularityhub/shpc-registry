---
layout: container
name:  "ruby"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ruby/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ruby/container.yaml"
updated_at: "2023-06-07 02:56:12.378470"
latest: "alpine3.18"
container_url: "https://hub.docker.com/_/ruby"
aliases:
 - "bundle"
 - "bundler"
 - "erb"
 - "gem"
 - "irb"
 - "racc"
 - "rake"
 - "rbs"
 - "rdoc"
 - "ri"
 - "ruby"
 - "typeprof"
versions:
 - "3.0.1-alpine"
 - "3.0.2"
 - "3.0.2-alpine"
 - "3.1.0"
 - "3.1.0-preview1"
 - "3.1.1"
 - "latest"
 - "3"
 - "3-alpine3.15"
 - "3.1"
 - "3.0.3"
 - "alpine"
 - "3.0.4"
 - "3-alpine3.16"
 - "3.0.4-alpine3.16"
 - "3.2-rc"
 - "3-alpine3.17"
 - "3.2"
 - "3.1.3"
 - "3.0"
 - "3.1.4"
 - "3-alpine3.18"
 - "alpine3.18"
description: "Ruby is a dynamic, reflective, object-oriented, general-purpose, open-source programming language."
config: {"docker": "ruby", "url": "https://hub.docker.com/_/ruby", "maintainer": "@vsoch", "description": "Ruby is a dynamic, reflective, object-oriented, general-purpose, open-source programming language.", "latest": {"alpine3.18": "sha256:1df6125b0f90e087123698e1b2df1c6a544a40033a5a14bfa3ef7067863d3474"}, "tags": {"3.0.1-alpine": "sha256:c7d2b6967cbf1d84477232ec8ad165585bed1f2cf8870eca86b3f90b1369313f", "3.0.2": "sha256:15dd21ae353c5f4faebed038d9d131c47b9fd84c14be8c3cfbc750204b63f009", "3.0.2-alpine": "sha256:b5e479ebc175726b5b77168b78b0322fec55e730c96f38ce8ca5b565aceca3a6", "3.1.0": "sha256:249deb7f2b1a01f034141f529a2daeecdfd2c04aa1e2b456bf328d899779ad7c", "3.1.0-preview1": "sha256:8740dc6f4d6468c6fc22f177c4159671ddd517f4ec3a7154549ffe1972d1f9a2", "3.1.1": "sha256:02132b99bb12b791701ae9bd86119eb879e49478b7b5d840c6c7cc9281ee63c0", "latest": "sha256:5efd846bccfafcabada226808406275e92269889467d571e897afc104e8c76c9", "3": "sha256:5efd846bccfafcabada226808406275e92269889467d571e897afc104e8c76c9", "3-alpine3.15": "sha256:3cd021fc8c763a5a5fc485eb6ca898eabdc5a94d1ac354511f5e958fc1cf3ca5", "3.1": "sha256:5bb1b8ce2f236cc264ae2f2664ec226603655b9129bd9442841a91fc6bb32313", "3.0.3": "sha256:7c57b474163e01f1518ff830dffef023fbd014378edd414526562137edc1400f", "alpine": "sha256:1df6125b0f90e087123698e1b2df1c6a544a40033a5a14bfa3ef7067863d3474", "3.0.4": "sha256:261fa5cfc39bfd39811a4f86f350e60aa3fa4e5a1ef68e92123f17e5c149e163", "3-alpine3.16": "sha256:8022d9a6f819976abf37747f44d8cc7e806bc2b111bac0aa7f846a1d1f6519da", "3.0.4-alpine3.16": "sha256:d5c7b1207fdfc7a39125c2a33929b974077f6cd1dfdaaca3750d114e5febf32e", "3.2-rc": "sha256:7a7d94375a7cfc3c2c9f46f1a2cc1ba432e88723a2166d815acd1cbbc44b2fa2", "3-alpine3.17": "sha256:b529c297be08b526c03d9f3d6911e13b15be7b9e25b992f4584e9208108bb132", "3.2": "sha256:5efd846bccfafcabada226808406275e92269889467d571e897afc104e8c76c9", "3.1.3": "sha256:c4d28f375a0addcf2d6fc0ac59e1f2d9d6ed5a2531568c1b80c35627bcae5b21", "3.0": "sha256:df252539300fd851c4c3f26d1d849686dd5c1bb46cf403e1d6a87d3d304a80f4", "3.1.4": "sha256:5bb1b8ce2f236cc264ae2f2664ec226603655b9129bd9442841a91fc6bb32313", "3-alpine3.18": "sha256:1df6125b0f90e087123698e1b2df1c6a544a40033a5a14bfa3ef7067863d3474", "alpine3.18": "sha256:1df6125b0f90e087123698e1b2df1c6a544a40033a5a14bfa3ef7067863d3474"}, "aliases": {"bundle": "/usr/local/bin/bundle", "bundler": "/usr/local/bin/bundler", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "racc": "/usr/local/bin/racc", "rake": "/usr/local/bin/rake", "rbs": "/usr/local/bin/rbs", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri", "ruby": "/usr/local/bin/ruby", "typeprof": "/usr/local/bin/typeprof"}}
---

This module is a singularity container wrapper for ruby.
Ruby is a dynamic, reflective, object-oriented, general-purpose, open-source programming language.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ruby
```

Or a specific version:

```bash
$ shpc install ruby:alpine3.18
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ruby/alpine3.18
$ module help ruby/alpine3.18
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ruby-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ruby-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ruby-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ruby-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ruby-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ruby-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bundle

```bash
$ singularity exec <container> /usr/local/bin/bundle
$ podman run --it --rm --entrypoint /usr/local/bin/bundle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundler

```bash
$ singularity exec <container> /usr/local/bin/bundler
$ podman run --it --rm --entrypoint /usr/local/bin/bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb

```bash
$ singularity exec <container> /usr/local/bin/erb
$ podman run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem

```bash
$ singularity exec <container> /usr/local/bin/gem
$ podman run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irb

```bash
$ singularity exec <container> /usr/local/bin/irb
$ podman run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racc

```bash
$ singularity exec <container> /usr/local/bin/racc
$ podman run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rake

```bash
$ singularity exec <container> /usr/local/bin/rake
$ podman run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbs

```bash
$ singularity exec <container> /usr/local/bin/rbs
$ podman run --it --rm --entrypoint /usr/local/bin/rbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdoc

```bash
$ singularity exec <container> /usr/local/bin/rdoc
$ podman run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ri

```bash
$ singularity exec <container> /usr/local/bin/ri
$ podman run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruby

```bash
$ singularity exec <container> /usr/local/bin/ruby
$ podman run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typeprof

```bash
$ singularity exec <container> /usr/local/bin/typeprof
$ podman run --it --rm --entrypoint /usr/local/bin/typeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
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