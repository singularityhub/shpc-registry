---
layout: container
name:  "quay.io/biocontainers/phame"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phame/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phame/container.yaml"
updated_at: "2023-06-12 05:15:37.157245"
latest: "1.0.3--1"
container_url: "https://biocontainers.pro/tools/phame"
aliases:
 - "CanSNPs.pl"
 - "ParseTree.pl"
 - "SNP_INDEL_count.pl"
 - "SNP_analysis.pl"
 - "buildSNPDB.pl"
 - "catAlign.pl"
 - "ccmake"
 - "checkNUCmer.pl"
 - "cmake"
 - "cpack"
 - "ctest"
 - "demuxbyname2.sh"
 - "ed2k-link"
 - "edonr256-hash"
 - "edonr512-hash"
 - "extractGenes.pl"
 - "get_repeat_coords.pl"
 - "gost-hash"
 - "has160-hash"
 - "hyphy"
 - "magnet-link"
 - "pal2nal.pl"
 - "parallel_run.pl"
 - "parseGapsNUCmer.pl"
 - "parseSitePAML.pl"
 - "phame"
 - "removeGaps.pl"
 - "removeRepeats.pl"
 - "rhash"
 - "runContigNUCmer.pl"
 - "runHyPhy.pl"
 - "runNUCmer.pl"
 - "runPAML.pl"
 - "runReadsMapping.pl"
 - "runReadsToGenome.pl"
 - "sfv-hash"
 - "tiger-hash"
 - "translate.pl"
 - "tth-hash"
 - "whirlpool-hash"
 - "addssu.sh"
 - "adjusthomopolymers.sh"
 - "analyzeaccession.sh"
 - "analyzegenes.sh"
 - "applyvariants.sh"
 - "bbcms.sh"
 - "bloomfilter.sh"
 - "callgenes.sh"
 - "comparegff.sh"
 - "consensus.sh"
versions:
 - "1.0.3--1"
description: "shpc-registry automated BioContainers addition for phame"
config: {"url": "https://biocontainers.pro/tools/phame", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phame", "latest": {"1.0.3--1": "sha256:d0ae5668a110eb4682329369f8b93f7cb692af7d64ab16e4e1de22274ec7a258"}, "tags": {"1.0.3--1": "sha256:d0ae5668a110eb4682329369f8b93f7cb692af7d64ab16e4e1de22274ec7a258"}, "docker": "quay.io/biocontainers/phame", "aliases": {"CanSNPs.pl": "/usr/local/bin/CanSNPs.pl", "ParseTree.pl": "/usr/local/bin/ParseTree.pl", "SNP_INDEL_count.pl": "/usr/local/bin/SNP_INDEL_count.pl", "SNP_analysis.pl": "/usr/local/bin/SNP_analysis.pl", "buildSNPDB.pl": "/usr/local/bin/buildSNPDB.pl", "catAlign.pl": "/usr/local/bin/catAlign.pl", "ccmake": "/usr/local/bin/ccmake", "checkNUCmer.pl": "/usr/local/bin/checkNUCmer.pl", "cmake": "/usr/local/bin/cmake", "cpack": "/usr/local/bin/cpack", "ctest": "/usr/local/bin/ctest", "demuxbyname2.sh": "/usr/local/bin/demuxbyname2.sh", "ed2k-link": "/usr/local/bin/ed2k-link", "edonr256-hash": "/usr/local/bin/edonr256-hash", "edonr512-hash": "/usr/local/bin/edonr512-hash", "extractGenes.pl": "/usr/local/bin/extractGenes.pl", "get_repeat_coords.pl": "/usr/local/bin/get_repeat_coords.pl", "gost-hash": "/usr/local/bin/gost-hash", "has160-hash": "/usr/local/bin/has160-hash", "hyphy": "/usr/local/bin/hyphy", "magnet-link": "/usr/local/bin/magnet-link", "pal2nal.pl": "/usr/local/bin/pal2nal.pl", "parallel_run.pl": "/usr/local/bin/parallel_run.pl", "parseGapsNUCmer.pl": "/usr/local/bin/parseGapsNUCmer.pl", "parseSitePAML.pl": "/usr/local/bin/parseSitePAML.pl", "phame": "/usr/local/bin/phame", "removeGaps.pl": "/usr/local/bin/removeGaps.pl", "removeRepeats.pl": "/usr/local/bin/removeRepeats.pl", "rhash": "/usr/local/bin/rhash", "runContigNUCmer.pl": "/usr/local/bin/runContigNUCmer.pl", "runHyPhy.pl": "/usr/local/bin/runHyPhy.pl", "runNUCmer.pl": "/usr/local/bin/runNUCmer.pl", "runPAML.pl": "/usr/local/bin/runPAML.pl", "runReadsMapping.pl": "/usr/local/bin/runReadsMapping.pl", "runReadsToGenome.pl": "/usr/local/bin/runReadsToGenome.pl", "sfv-hash": "/usr/local/bin/sfv-hash", "tiger-hash": "/usr/local/bin/tiger-hash", "translate.pl": "/usr/local/bin/translate.pl", "tth-hash": "/usr/local/bin/tth-hash", "whirlpool-hash": "/usr/local/bin/whirlpool-hash", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "analyzeaccession.sh": "/usr/local/bin/analyzeaccession.sh", "analyzegenes.sh": "/usr/local/bin/analyzegenes.sh", "applyvariants.sh": "/usr/local/bin/applyvariants.sh", "bbcms.sh": "/usr/local/bin/bbcms.sh", "bloomfilter.sh": "/usr/local/bin/bloomfilter.sh", "callgenes.sh": "/usr/local/bin/callgenes.sh", "comparegff.sh": "/usr/local/bin/comparegff.sh", "consensus.sh": "/usr/local/bin/consensus.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phame.
shpc-registry automated BioContainers addition for phame
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phame
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phame:1.0.3--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phame/1.0.3--1
$ module help quay.io/biocontainers/phame/1.0.3--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phame-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phame-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phame-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phame-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phame-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phame-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CanSNPs.pl

```bash
$ singularity exec <container> /usr/local/bin/CanSNPs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/CanSNPs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CanSNPs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ParseTree.pl

```bash
$ singularity exec <container> /usr/local/bin/ParseTree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ParseTree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ParseTree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SNP_INDEL_count.pl

```bash
$ singularity exec <container> /usr/local/bin/SNP_INDEL_count.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SNP_INDEL_count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SNP_INDEL_count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SNP_analysis.pl

```bash
$ singularity exec <container> /usr/local/bin/SNP_analysis.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SNP_analysis.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SNP_analysis.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSNPDB.pl

```bash
$ singularity exec <container> /usr/local/bin/buildSNPDB.pl
$ podman run --it --rm --entrypoint /usr/local/bin/buildSNPDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSNPDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### catAlign.pl

```bash
$ singularity exec <container> /usr/local/bin/catAlign.pl
$ podman run --it --rm --entrypoint /usr/local/bin/catAlign.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catAlign.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccmake

```bash
$ singularity exec <container> /usr/local/bin/ccmake
$ podman run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkNUCmer.pl

```bash
$ singularity exec <container> /usr/local/bin/checkNUCmer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/checkNUCmer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkNUCmer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmake

```bash
$ singularity exec <container> /usr/local/bin/cmake
$ podman run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpack

```bash
$ singularity exec <container> /usr/local/bin/cpack
$ podman run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ctest

```bash
$ singularity exec <container> /usr/local/bin/ctest
$ podman run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demuxbyname2.sh

```bash
$ singularity exec <container> /usr/local/bin/demuxbyname2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/demuxbyname2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demuxbyname2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ed2k-link

```bash
$ singularity exec <container> /usr/local/bin/ed2k-link
$ podman run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edonr256-hash

```bash
$ singularity exec <container> /usr/local/bin/edonr256-hash
$ podman run --it --rm --entrypoint /usr/local/bin/edonr256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edonr256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edonr512-hash

```bash
$ singularity exec <container> /usr/local/bin/edonr512-hash
$ podman run --it --rm --entrypoint /usr/local/bin/edonr512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edonr512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractGenes.pl

```bash
$ singularity exec <container> /usr/local/bin/extractGenes.pl
$ podman run --it --rm --entrypoint /usr/local/bin/extractGenes.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractGenes.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_repeat_coords.pl

```bash
$ singularity exec <container> /usr/local/bin/get_repeat_coords.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_repeat_coords.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_repeat_coords.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gost-hash

```bash
$ singularity exec <container> /usr/local/bin/gost-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### has160-hash

```bash
$ singularity exec <container> /usr/local/bin/has160-hash
$ podman run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hyphy

```bash
$ singularity exec <container> /usr/local/bin/hyphy
$ podman run --it --rm --entrypoint /usr/local/bin/hyphy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hyphy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magnet-link

```bash
$ singularity exec <container> /usr/local/bin/magnet-link
$ podman run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pal2nal.pl

```bash
$ singularity exec <container> /usr/local/bin/pal2nal.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pal2nal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pal2nal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel_run.pl

```bash
$ singularity exec <container> /usr/local/bin/parallel_run.pl
$ podman run --it --rm --entrypoint /usr/local/bin/parallel_run.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel_run.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parseGapsNUCmer.pl

```bash
$ singularity exec <container> /usr/local/bin/parseGapsNUCmer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/parseGapsNUCmer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parseGapsNUCmer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parseSitePAML.pl

```bash
$ singularity exec <container> /usr/local/bin/parseSitePAML.pl
$ podman run --it --rm --entrypoint /usr/local/bin/parseSitePAML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parseSitePAML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phame

```bash
$ singularity exec <container> /usr/local/bin/phame
$ podman run --it --rm --entrypoint /usr/local/bin/phame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### removeGaps.pl

```bash
$ singularity exec <container> /usr/local/bin/removeGaps.pl
$ podman run --it --rm --entrypoint /usr/local/bin/removeGaps.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/removeGaps.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### removeRepeats.pl

```bash
$ singularity exec <container> /usr/local/bin/removeRepeats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/removeRepeats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/removeRepeats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rhash

```bash
$ singularity exec <container> /usr/local/bin/rhash
$ podman run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runContigNUCmer.pl

```bash
$ singularity exec <container> /usr/local/bin/runContigNUCmer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/runContigNUCmer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runContigNUCmer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runHyPhy.pl

```bash
$ singularity exec <container> /usr/local/bin/runHyPhy.pl
$ podman run --it --rm --entrypoint /usr/local/bin/runHyPhy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runHyPhy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runNUCmer.pl

```bash
$ singularity exec <container> /usr/local/bin/runNUCmer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/runNUCmer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runNUCmer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runPAML.pl

```bash
$ singularity exec <container> /usr/local/bin/runPAML.pl
$ podman run --it --rm --entrypoint /usr/local/bin/runPAML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runPAML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runReadsMapping.pl

```bash
$ singularity exec <container> /usr/local/bin/runReadsMapping.pl
$ podman run --it --rm --entrypoint /usr/local/bin/runReadsMapping.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runReadsMapping.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runReadsToGenome.pl

```bash
$ singularity exec <container> /usr/local/bin/runReadsToGenome.pl
$ podman run --it --rm --entrypoint /usr/local/bin/runReadsToGenome.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runReadsToGenome.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfv-hash

```bash
$ singularity exec <container> /usr/local/bin/sfv-hash
$ podman run --it --rm --entrypoint /usr/local/bin/sfv-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfv-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiger-hash

```bash
$ singularity exec <container> /usr/local/bin/tiger-hash
$ podman run --it --rm --entrypoint /usr/local/bin/tiger-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiger-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### translate.pl

```bash
$ singularity exec <container> /usr/local/bin/translate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/translate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/translate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tth-hash

```bash
$ singularity exec <container> /usr/local/bin/tth-hash
$ podman run --it --rm --entrypoint /usr/local/bin/tth-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tth-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whirlpool-hash

```bash
$ singularity exec <container> /usr/local/bin/whirlpool-hash
$ podman run --it --rm --entrypoint /usr/local/bin/whirlpool-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whirlpool-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addssu.sh

```bash
$ singularity exec <container> /usr/local/bin/addssu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adjusthomopolymers.sh

```bash
$ singularity exec <container> /usr/local/bin/adjusthomopolymers.sh
$ podman run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzeaccession.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzeaccession.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzegenes.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzegenes.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### applyvariants.sh

```bash
$ singularity exec <container> /usr/local/bin/applyvariants.sh
$ podman run --it --rm --entrypoint /usr/local/bin/applyvariants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/applyvariants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbcms.sh

```bash
$ singularity exec <container> /usr/local/bin/bbcms.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bbcms.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbcms.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bloomfilter.sh

```bash
$ singularity exec <container> /usr/local/bin/bloomfilter.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bloomfilter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bloomfilter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### callgenes.sh

```bash
$ singularity exec <container> /usr/local/bin/callgenes.sh
$ podman run --it --rm --entrypoint /usr/local/bin/callgenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/callgenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comparegff.sh

```bash
$ singularity exec <container> /usr/local/bin/comparegff.sh
$ podman run --it --rm --entrypoint /usr/local/bin/comparegff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comparegff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus.sh

```bash
$ singularity exec <container> /usr/local/bin/consensus.sh
$ podman run --it --rm --entrypoint /usr/local/bin/consensus.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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