---
layout: container
name:  "quay.io/biocontainers/funtaxfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/funtaxfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/funtaxfinder/container.yaml"
updated_at: "2026-06-23 16:36:37.380734"
latest: "0.1.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/funtaxfinder"
aliases:
 - "add_descriptions.py"
 - "add_descriptions_oldIMG.py"
 - "combine_domains.py"
 - "convert_table.py"
 - "count_hmm_hits.py"
 - "epa-ng"
 - "funtaxfinder"
 - "gappa"
 - "hsp.py"
 - "metagenome_pipeline.py"
 - "pathway_pipeline.py"
 - "pick_best_domain.py"
 - "picrust2_pipeline.py"
 - "picrust2_pipeline_singleRef.py"
 - "place_seqs.py"
 - "shuffle_predictions.py"
 - "run-sepp.sh"
 - "run_sepp.py"
 - "run_upp.py"
 - "seppJsonMerger.jar"
 - "split_sequences.py"
 - "treeshrink"
 - "gawk-5.4.0"
 - "hmmerbuild"
 - "fc-genconf"
 - "hmmeralign"
 - "opal.jar"
 - "raxml"
 - "run_pasta.py"
 - "run_pasta_gui.py"
 - "run_seqtools.py"
 - "sumlabels"
 - "sumtrees"
 - "coverage"
 - "jnativescan"
 - "prank"
 - "guppy"
 - "pplacer"
 - "pax11publish"
 - "biom"
 - "raxmlHPC"
versions:
 - "0.1.0--pyhdfd78af_1"
description: "singularity registry hpc automated addition for funtaxfinder"
config: {"url": "https://biocontainers.pro/tools/funtaxfinder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for funtaxfinder", "latest": {"0.1.0--pyhdfd78af_1": "sha256:b519fd5529bef5337c5964bb8ca8814039cf4108f2a10dd4bc7aa9b5c316e41a"}, "tags": {"0.1.0--pyhdfd78af_1": "sha256:b519fd5529bef5337c5964bb8ca8814039cf4108f2a10dd4bc7aa9b5c316e41a"}, "docker": "quay.io/biocontainers/funtaxfinder", "aliases": {"add_descriptions.py": "/usr/local/bin/add_descriptions.py", "add_descriptions_oldIMG.py": "/usr/local/bin/add_descriptions_oldIMG.py", "combine_domains.py": "/usr/local/bin/combine_domains.py", "convert_table.py": "/usr/local/bin/convert_table.py", "count_hmm_hits.py": "/usr/local/bin/count_hmm_hits.py", "epa-ng": "/usr/local/bin/epa-ng", "funtaxfinder": "/usr/local/bin/funtaxfinder", "gappa": "/usr/local/bin/gappa", "hsp.py": "/usr/local/bin/hsp.py", "metagenome_pipeline.py": "/usr/local/bin/metagenome_pipeline.py", "pathway_pipeline.py": "/usr/local/bin/pathway_pipeline.py", "pick_best_domain.py": "/usr/local/bin/pick_best_domain.py", "picrust2_pipeline.py": "/usr/local/bin/picrust2_pipeline.py", "picrust2_pipeline_singleRef.py": "/usr/local/bin/picrust2_pipeline_singleRef.py", "place_seqs.py": "/usr/local/bin/place_seqs.py", "shuffle_predictions.py": "/usr/local/bin/shuffle_predictions.py", "run-sepp.sh": "/usr/local/bin/run-sepp.sh", "run_sepp.py": "/usr/local/bin/run_sepp.py", "run_upp.py": "/usr/local/bin/run_upp.py", "seppJsonMerger.jar": "/usr/local/bin/seppJsonMerger.jar", "split_sequences.py": "/usr/local/bin/split_sequences.py", "treeshrink": "/usr/local/bin/treeshrink", "gawk-5.4.0": "/usr/local/bin/gawk-5.4.0", "hmmerbuild": "/usr/local/bin/hmmerbuild", "fc-genconf": "/usr/local/bin/fc-genconf", "hmmeralign": "/usr/local/bin/hmmeralign", "opal.jar": "/usr/local/bin/opal.jar", "raxml": "/usr/local/bin/raxml", "run_pasta.py": "/usr/local/bin/run_pasta.py", "run_pasta_gui.py": "/usr/local/bin/run_pasta_gui.py", "run_seqtools.py": "/usr/local/bin/run_seqtools.py", "sumlabels": "/usr/local/bin/sumlabels", "sumtrees": "/usr/local/bin/sumtrees", "coverage": "/usr/local/bin/coverage", "jnativescan": "/usr/local/bin/jnativescan", "prank": "/usr/local/bin/prank", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer", "pax11publish": "/usr/local/bin/pax11publish", "biom": "/usr/local/bin/biom", "raxmlHPC": "/usr/local/bin/raxmlHPC"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/funtaxfinder.
singularity registry hpc automated addition for funtaxfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/funtaxfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/funtaxfinder:0.1.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/funtaxfinder/0.1.0--pyhdfd78af_1
$ module help quay.io/biocontainers/funtaxfinder/0.1.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### funtaxfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### funtaxfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### funtaxfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### funtaxfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### funtaxfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### funtaxfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_descriptions.py

```bash
$ singularity exec <container> /usr/local/bin/add_descriptions.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_descriptions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_descriptions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### add_descriptions_oldIMG.py

```bash
$ singularity exec <container> /usr/local/bin/add_descriptions_oldIMG.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_descriptions_oldIMG.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_descriptions_oldIMG.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_domains.py

```bash
$ singularity exec <container> /usr/local/bin/combine_domains.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_domains.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_domains.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_table.py

```bash
$ singularity exec <container> /usr/local/bin/convert_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count_hmm_hits.py

```bash
$ singularity exec <container> /usr/local/bin/count_hmm_hits.py
$ podman run --it --rm --entrypoint /usr/local/bin/count_hmm_hits.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count_hmm_hits.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### epa-ng

```bash
$ singularity exec <container> /usr/local/bin/epa-ng
$ podman run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funtaxfinder

```bash
$ singularity exec <container> /usr/local/bin/funtaxfinder
$ podman run --it --rm --entrypoint /usr/local/bin/funtaxfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funtaxfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gappa

```bash
$ singularity exec <container> /usr/local/bin/gappa
$ podman run --it --rm --entrypoint /usr/local/bin/gappa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gappa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsp.py

```bash
$ singularity exec <container> /usr/local/bin/hsp.py
$ podman run --it --rm --entrypoint /usr/local/bin/hsp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metagenome_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/metagenome_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/metagenome_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metagenome_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathway_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/pathway_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/pathway_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathway_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pick_best_domain.py

```bash
$ singularity exec <container> /usr/local/bin/pick_best_domain.py
$ podman run --it --rm --entrypoint /usr/local/bin/pick_best_domain.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pick_best_domain.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picrust2_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/picrust2_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/picrust2_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picrust2_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picrust2_pipeline_singleRef.py

```bash
$ singularity exec <container> /usr/local/bin/picrust2_pipeline_singleRef.py
$ podman run --it --rm --entrypoint /usr/local/bin/picrust2_pipeline_singleRef.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picrust2_pipeline_singleRef.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### place_seqs.py

```bash
$ singularity exec <container> /usr/local/bin/place_seqs.py
$ podman run --it --rm --entrypoint /usr/local/bin/place_seqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/place_seqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffle_predictions.py

```bash
$ singularity exec <container> /usr/local/bin/shuffle_predictions.py
$ podman run --it --rm --entrypoint /usr/local/bin/shuffle_predictions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffle_predictions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-sepp.sh

```bash
$ singularity exec <container> /usr/local/bin/run-sepp.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run-sepp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-sepp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_sepp.py

```bash
$ singularity exec <container> /usr/local/bin/run_sepp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_sepp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_sepp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_upp.py

```bash
$ singularity exec <container> /usr/local/bin/run_upp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_upp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_upp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seppJsonMerger.jar

```bash
$ singularity exec <container> /usr/local/bin/seppJsonMerger.jar
$ podman run --it --rm --entrypoint /usr/local/bin/seppJsonMerger.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seppJsonMerger.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_sequences.py

```bash
$ singularity exec <container> /usr/local/bin/split_sequences.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treeshrink

```bash
$ singularity exec <container> /usr/local/bin/treeshrink
$ podman run --it --rm --entrypoint /usr/local/bin/treeshrink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treeshrink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerbuild

```bash
$ singularity exec <container> /usr/local/bin/hmmerbuild
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmeralign

```bash
$ singularity exec <container> /usr/local/bin/hmmeralign
$ podman run --it --rm --entrypoint /usr/local/bin/hmmeralign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmeralign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opal.jar

```bash
$ singularity exec <container> /usr/local/bin/opal.jar
$ podman run --it --rm --entrypoint /usr/local/bin/opal.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opal.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml

```bash
$ singularity exec <container> /usr/local/bin/raxml
$ podman run --it --rm --entrypoint /usr/local/bin/raxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_pasta.py

```bash
$ singularity exec <container> /usr/local/bin/run_pasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_pasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_pasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_pasta_gui.py

```bash
$ singularity exec <container> /usr/local/bin/run_pasta_gui.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_pasta_gui.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_pasta_gui.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_seqtools.py

```bash
$ singularity exec <container> /usr/local/bin/run_seqtools.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_seqtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_seqtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels

```bash
$ singularity exec <container> /usr/local/bin/sumlabels
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees

```bash
$ singularity exec <container> /usr/local/bin/sumtrees
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage

```bash
$ singularity exec <container> /usr/local/bin/coverage
$ podman run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jnativescan

```bash
$ singularity exec <container> /usr/local/bin/jnativescan
$ podman run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prank

```bash
$ singularity exec <container> /usr/local/bin/prank
$ podman run --it --rm --entrypoint /usr/local/bin/prank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guppy

```bash
$ singularity exec <container> /usr/local/bin/guppy
$ podman run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pplacer

```bash
$ singularity exec <container> /usr/local/bin/pplacer
$ podman run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pax11publish

```bash
$ singularity exec <container> /usr/local/bin/pax11publish
$ podman run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom

```bash
$ singularity exec <container> /usr/local/bin/biom
$ podman run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
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