#ifndef ANIMATIONS_H
#define ANIMATIONS_H

#include "pharaohAnimatable.h"

namespace visualizer
{
  class DrawFadedObject : public Anim
  {
  public:
    DrawFadedObject(const Color& start, const Color& end, FadeFlag fade) : m_start(start), m_end(end), m_fade(fade) {}

    void animate(const float &t, AnimData *d, IGame *game);
  private:
    Color m_start;
    Color m_end;
    FadeFlag m_fade;
  };

#define DRAW_OBJECT(nameClass, dataClass) \
  class nameClass: public DrawFadedObject \
  { \
    public: \
      nameClass( dataClass* data, const Color& start, const Color& end, FadeFlag fade = None ) : DrawFadedObject(start, end, fade) { m_data = data; } \
      void animate( const float& t, AnimData* d, IGame* game ); \
    private: \
      dataClass *m_data; \
  };
  
  DRAW_OBJECT(DrawQuad, DrawQuadData)
  DRAW_OBJECT(DrawWinningScreen, DrawWinningData)
  DRAW_OBJECT(DrawSprite, DrawSpriteData)
  DRAW_OBJECT(DrawAnimatedSprite, DrawAnimatedSpriteData)
  DRAW_OBJECT(DrawScreenText, DrawScreenTextData)
}

#endif // ANIMATION_H
