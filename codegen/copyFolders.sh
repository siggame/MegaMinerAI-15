#! /bin/bash
cp -r output/python ../clients
cp -r output/cpp ../clients
cp -r output/java ../clients
cp -r output/csharp ../clients
cp -r output/library ../clients

# Client repos
for lang in $(echo "python cpp java csharp"); do
  if [ ! -d ../../pharaoh-$lang ]; then
    git -C ../.. clone git@github.com:siggame/pharaoh-$lang
  fi
  cp -r output/$lang/* ../../pharaoh-$lang
  cp -r output/library ../../pharaoh-$lang
  git -C ../../pharaoh-$lang checkout -- Makefile
done
