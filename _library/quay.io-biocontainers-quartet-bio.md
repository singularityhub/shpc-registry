---
layout: container
name:  "quay.io/biocontainers/quartet-bio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/quartet-bio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/quartet-bio/container.yaml"
updated_at: "2026-04-26 06:00:42.840341"
latest: "1.2.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/quartet-bio"
aliases:
 - "hifiasm"
 - "minitest"
 - "quartet.py"
 - "quartet_assemblymapper.py"
 - "quartet_centrominer.py"
 - "quartet_gapfiller.py"
 - "quartet_teloexplorer.py"
 - "quartet_util.py"
 - "setup.py"
 - "syntax_suggest"
 - "test-unit"
 - "tidk"
 - "unimap"
 - "yaggo"
 - "rbs"
 - "rdbg"
 - "typeprof"
 - "racc"
 - "bundle"
 - "bundler"
 - "trf"
 - "gnuplot"
 - "pax11publish"
 - "archive-nlmnlp"
 - "archive-pids"
 - "download-flatfile"
 - "ecollect"
 - "erb"
 - "gbf2facds"
 - "gbf2tbl"
 - "gem"
 - "gff-sort"
 - "gff2xml"
 - "irb"
 - "pair-at-a-time"
 - "print-missing-subranges"
 - "rake"
 - "rdoc"
 - "ri"
versions:
 - "1.2.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for quartet-bio"
config: {"url": "https://biocontainers.pro/tools/quartet-bio", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for quartet-bio", "latest": {"1.2.5--pyhdfd78af_0": "sha256:73e4ab045a514e53e5400c7b3033fb1c4dc277f34e797e67bc913473079458a5"}, "tags": {"1.2.5--pyhdfd78af_0": "sha256:73e4ab045a514e53e5400c7b3033fb1c4dc277f34e797e67bc913473079458a5"}, "docker": "quay.io/biocontainers/quartet-bio", "aliases": {"hifiasm": "/usr/local/bin/hifiasm", "minitest": "/usr/local/bin/minitest", "quartet.py": "/usr/local/bin/quartet.py", "quartet_assemblymapper.py": "/usr/local/bin/quartet_assemblymapper.py", "quartet_centrominer.py": "/usr/local/bin/quartet_centrominer.py", "quartet_gapfiller.py": "/usr/local/bin/quartet_gapfiller.py", "quartet_teloexplorer.py": "/usr/local/bin/quartet_teloexplorer.py", "quartet_util.py": "/usr/local/bin/quartet_util.py", "setup.py": "/usr/local/bin/setup.py", "syntax_suggest": "/usr/local/bin/syntax_suggest", "test-unit": "/usr/local/bin/test-unit", "tidk": "/usr/local/bin/tidk", "unimap": "/usr/local/bin/unimap", "yaggo": "/usr/local/bin/yaggo", "rbs": "/usr/local/bin/rbs", "rdbg": "/usr/local/bin/rdbg", "typeprof": "/usr/local/bin/typeprof", "racc": "/usr/local/bin/racc", "bundle": "/usr/local/bin/bundle", "bundler": "/usr/local/bin/bundler", "trf": "/usr/local/bin/trf", "gnuplot": "/usr/local/bin/gnuplot", "pax11publish": "/usr/local/bin/pax11publish", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "erb": "/usr/local/bin/erb", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gem": "/usr/local/bin/gem", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "irb": "/usr/local/bin/irb", "pair-at-a-time": "/usr/local/bin/pair-at-a-time", "print-missing-subranges": "/usr/local/bin/print-missing-subranges", "rake": "/usr/local/bin/rake", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/quartet-bio.
singularity registry hpc automated addition for quartet-bio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/quartet-bio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/quartet-bio:1.2.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/quartet-bio/1.2.5--pyhdfd78af_0
$ module help quay.io/biocontainers/quartet-bio/1.2.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quartet-bio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quartet-bio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quartet-bio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quartet-bio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quartet-bio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quartet-bio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hifiasm

```bash
$ singularity exec <container> /usr/local/bin/hifiasm
$ podman run --it --rm --entrypoint /usr/local/bin/hifiasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hifiasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minitest

```bash
$ singularity exec <container> /usr/local/bin/minitest
$ podman run --it --rm --entrypoint /usr/local/bin/minitest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minitest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quartet.py

```bash
$ singularity exec <container> /usr/local/bin/quartet.py
$ podman run --it --rm --entrypoint /usr/local/bin/quartet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quartet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quartet_assemblymapper.py

```bash
$ singularity exec <container> /usr/local/bin/quartet_assemblymapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/quartet_assemblymapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quartet_assemblymapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quartet_centrominer.py

```bash
$ singularity exec <container> /usr/local/bin/quartet_centrominer.py
$ podman run --it --rm --entrypoint /usr/local/bin/quartet_centrominer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quartet_centrominer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quartet_gapfiller.py

```bash
$ singularity exec <container> /usr/local/bin/quartet_gapfiller.py
$ podman run --it --rm --entrypoint /usr/local/bin/quartet_gapfiller.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quartet_gapfiller.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quartet_teloexplorer.py

```bash
$ singularity exec <container> /usr/local/bin/quartet_teloexplorer.py
$ podman run --it --rm --entrypoint /usr/local/bin/quartet_teloexplorer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quartet_teloexplorer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quartet_util.py

```bash
$ singularity exec <container> /usr/local/bin/quartet_util.py
$ podman run --it --rm --entrypoint /usr/local/bin/quartet_util.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quartet_util.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup.py

```bash
$ singularity exec <container> /usr/local/bin/setup.py
$ podman run --it --rm --entrypoint /usr/local/bin/setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### syntax_suggest

```bash
$ singularity exec <container> /usr/local/bin/syntax_suggest
$ podman run --it --rm --entrypoint /usr/local/bin/syntax_suggest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/syntax_suggest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test-unit

```bash
$ singularity exec <container> /usr/local/bin/test-unit
$ podman run --it --rm --entrypoint /usr/local/bin/test-unit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test-unit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tidk

```bash
$ singularity exec <container> /usr/local/bin/tidk
$ podman run --it --rm --entrypoint /usr/local/bin/tidk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tidk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unimap

```bash
$ singularity exec <container> /usr/local/bin/unimap
$ podman run --it --rm --entrypoint /usr/local/bin/unimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yaggo

```bash
$ singularity exec <container> /usr/local/bin/yaggo
$ podman run --it --rm --entrypoint /usr/local/bin/yaggo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yaggo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbs

```bash
$ singularity exec <container> /usr/local/bin/rbs
$ podman run --it --rm --entrypoint /usr/local/bin/rbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdbg

```bash
$ singularity exec <container> /usr/local/bin/rdbg
$ podman run --it --rm --entrypoint /usr/local/bin/rdbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdbg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typeprof

```bash
$ singularity exec <container> /usr/local/bin/typeprof
$ podman run --it --rm --entrypoint /usr/local/bin/typeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racc

```bash
$ singularity exec <container> /usr/local/bin/racc
$ podman run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### trf

```bash
$ singularity exec <container> /usr/local/bin/trf
$ podman run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnuplot

```bash
$ singularity exec <container> /usr/local/bin/gnuplot
$ podman run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pax11publish

```bash
$ singularity exec <container> /usr/local/bin/pax11publish
$ podman run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nlmnlp

```bash
$ singularity exec <container> /usr/local/bin/archive-nlmnlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pids

```bash
$ singularity exec <container> /usr/local/bin/archive-pids
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-flatfile

```bash
$ singularity exec <container> /usr/local/bin/download-flatfile
$ podman run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecollect

```bash
$ singularity exec <container> /usr/local/bin/ecollect
$ podman run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb

```bash
$ singularity exec <container> /usr/local/bin/erb
$ podman run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2facds

```bash
$ singularity exec <container> /usr/local/bin/gbf2facds
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2tbl

```bash
$ singularity exec <container> /usr/local/bin/gbf2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem

```bash
$ singularity exec <container> /usr/local/bin/gem
$ podman run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff-sort

```bash
$ singularity exec <container> /usr/local/bin/gff-sort
$ podman run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2xml

```bash
$ singularity exec <container> /usr/local/bin/gff2xml
$ podman run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irb

```bash
$ singularity exec <container> /usr/local/bin/irb
$ podman run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pair-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/pair-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print-missing-subranges

```bash
$ singularity exec <container> /usr/local/bin/print-missing-subranges
$ podman run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rake

```bash
$ singularity exec <container> /usr/local/bin/rake
$ podman run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
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