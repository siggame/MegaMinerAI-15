#ifndef PHARAOH_ANIMATABLE_H
#define PHARAOH_ANIMATABLE_H

//#include "pharaohAnimatable.h"
#include "irenderer.h"
#include "parser/structures.h"

#include "math.h"
#include <glm/glm.hpp>

namespace visualizer
{
  enum FadeFlag
  {
    FadeIn,
    FadeOut,
    None
  };

  struct DrawQuadData : public Animatable
  {
    DrawQuadData(float x, float y, float width, float height) :
      x(x), y(y), width(width), height(height) {}
    
      float x, y;
      float width, height;
  };
    
  struct DrawWinningData : public DrawQuadData
  {
    DrawWinningData(float x, float y, float width, float height, string winner) :
    DrawQuadData(x, y, width, height), winner(winner){}
  
    string winner;
  };
  
  struct DrawSpriteData : public Animatable
  {
    DrawSpriteData(float x, float y, float width, float height, string texture, bool flip) :
      x(x), y(y), width(width), height(height), texture(texture), flip(flip){}
  
    float x, y;
    float width, height;
    string texture;
    bool flip;
  };

  struct DrawAnimatedSpriteData : public DrawSpriteData
  {
    DrawAnimatedSpriteData(int startFrame, int endFrame,
                           float x, float y,
                          float width, float height, string texture, bool flip) :
      DrawSpriteData(x, y, width, height, texture, flip), startFrame(startFrame), endFrame(endFrame){}

    int startFrame;
    int endFrame;
  };

  struct DrawScreenTextData : public Animatable
  {
      DrawScreenTextData(float x, float y, float width, float height, string text) :
          x(x), y(y), width(width), height(height), text(text.substr(0,20) ) {}

      float x, y, width, height;
      string text;

  };
} // visualizer
#endif // PHARAOH_ANIMATABLE_H
