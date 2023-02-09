---
layout: container
name:  "ruby"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ruby/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ruby/container.yaml"
updated_at: "2023-02-09 02:48:53.964736"
latest: "3-alpine3.17"
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
description: "Ruby is a dynamic, reflective, object-oriented, general-purpose, open-source programming language."
config: {"docker": "ruby", "url": "https://hub.docker.com/_/ruby", "maintainer": "@vsoch", "description": "Ruby is a dynamic, reflective, object-oriented, general-purpose, open-source programming language.", "latest": {"3-alpine3.17": "sha256:c690d3b45ef65e0098104c272f1736b0595b824908d5639c3a3d17636581a905"}, "tags": {"3.0.1-alpine": "sha256:c7d2b6967cbf1d84477232ec8ad165585bed1f2cf8870eca86b3f90b1369313f", "3.0.2": "sha256:15dd21ae353c5f4faebed038d9d131c47b9fd84c14be8c3cfbc750204b63f009", "3.0.2-alpine": "sha256:b5e479ebc175726b5b77168b78b0322fec55e730c96f38ce8ca5b565aceca3a6", "3.1.0": "sha256:249deb7f2b1a01f034141f529a2daeecdfd2c04aa1e2b456bf328d899779ad7c", "3.1.0-preview1": "sha256:8740dc6f4d6468c6fc22f177c4159671ddd517f4ec3a7154549ffe1972d1f9a2", "3.1.1": "sha256:02132b99bb12b791701ae9bd86119eb879e49478b7b5d840c6c7cc9281ee63c0", "latest": "sha256:a4e5963a2dfcddc1ebc65c7118b814c4639c711eb5a478562581beaac8999f69", "3": "sha256:a4e5963a2dfcddc1ebc65c7118b814c4639c711eb5a478562581beaac8999f69", "3-alpine3.15": "sha256:3cd021fc8c763a5a5fc485eb6ca898eabdc5a94d1ac354511f5e958fc1cf3ca5", "3.1": "sha256:3e1c037993632f59558a2a3b80071e679e88dc4f9416c9f02faa17638fe30b6e", "3.0.3": "sha256:7c57b474163e01f1518ff830dffef023fbd014378edd414526562137edc1400f", "alpine": "sha256:c690d3b45ef65e0098104c272f1736b0595b824908d5639c3a3d17636581a905", "3.0.4": "sha256:261fa5cfc39bfd39811a4f86f350e60aa3fa4e5a1ef68e92123f17e5c149e163", "3-alpine3.16": "sha256:fee65eb1192eaafb7d6f548b385af555b0bae665d35fdb0092963030ff9ec354", "3.0.4-alpine3.16": "sha256:d5c7b1207fdfc7a39125c2a33929b974077f6cd1dfdaaca3750d114e5febf32e", "3.2-rc": "sha256:7a7d94375a7cfc3c2c9f46f1a2cc1ba432e88723a2166d815acd1cbbc44b2fa2", "3-alpine3.17": "sha256:c690d3b45ef65e0098104c272f1736b0595b824908d5639c3a3d17636581a905", "3.2": "sha256:a4e5963a2dfcddc1ebc65c7118b814c4639c711eb5a478562581beaac8999f69", "3.1.3": "sha256:3e1c037993632f59558a2a3b80071e679e88dc4f9416c9f02faa17638fe30b6e"}, "aliases": {"bundle": "/usr/local/bin/bundle", "bundler": "/usr/local/bin/bundler", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "racc": "/usr/local/bin/racc", "rake": "/usr/local/bin/rake", "rbs": "/usr/local/bin/rbs", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri", "ruby": "/usr/local/bin/ruby", "typeprof": "/usr/local/bin/typeprof"}}
---

This module is a singularity container wrapper for ruby.
Ruby is a dynamic, reflective, object-oriented, general-purpose, open-source programming language.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ruby
```

Or a specific version:

```bash
$ shpc install ruby:3-alpine3.17
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ruby/3-alpine3.17
$ module help ruby/3-alpine3.17
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