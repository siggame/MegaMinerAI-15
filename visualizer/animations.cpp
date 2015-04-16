#include "animations.h"
#include "pharaoh.h"
#include <glm/glm.hpp>

namespace visualizer
{
  void DrawFadedObject::animate(const float &t, AnimData *d, IGame *game)
  {
     glm::vec4 vecColor = glm::mix(glm::vec4(m_start.r, m_start.g, m_start.b, m_start.a), glm::vec4(m_end.r, m_end.g, m_end.b, m_end.a), t);
    // Set the color to red
    float scalar = t;
    if(m_fade == FadeIn)
    {
      scalar = t;
    }
    else if(m_fade == FadeOut)
    {
      scalar = 1 - t;
    }
    else
    {
      scalar = 1.0f;
    }

    //float color = m_data->fade
    game->renderer->setColor(Color(vecColor.r, vecColor.g, vecColor.b, vecColor.a * scalar));
  }

  void DrawQuad::animate( const float& t, AnimData* d, IGame* game )
  {
    DrawFadedObject::animate(t, d, game);

    game->pushZoomMatrix();
    game->renderer->drawQuad( m_data->x, m_data->y, m_data->width * (1/game->zoomFactor()), m_data->height * (1/game->zoomFactor()) );
    game->popZoomMatrix();
  }

  void DrawWinningScreen::animate( const float& t, AnimData* d, IGame* game )
  {
    DrawFadedObject::animate(t, d, game);

    game->renderer->drawQuad( m_data->x, m_data->y, m_data->width, m_data->height );
    game->renderer->setColor(Color(1.0f, 1.0f, 1.0f, 1.0f));
    game->renderer->drawText( m_data->x + (m_data->width)/2, m_data->y + (m_data->height)/2, "Roboto", m_data->winner, 200.0f, IRenderer::Center);
  }

  void DrawSprite::animate( const float& t, AnimData* d, IGame* game )
  {
    DrawFadedObject::animate(t, d, game);
    
    game->pushZoomMatrix();
    float x, y, w, h;
    w = m_data->width;// * (1/game->zoomFactor());
    h = m_data->height;// * (1/game->zoomFactor());
    x = m_data->x + ((m_data->width/2) - (w/2));
    y = m_data->y + ((m_data->height/2) - (h/2));
    game->renderer->drawTexturedQuad(x, y, w, h, 1.0f, m_data->texture, m_data->flip );
    game->popZoomMatrix();
  }

  void DrawAnimatedSprite::animate(const float &t, AnimData *d, IGame *game)
  {
    DrawFadedObject::animate(t, d, game);

    game->pushZoomMatrix();
    
    float x,y, w, h;
    w = m_data->width * (1/game->zoomFactor());
    h = m_data->height * (1/game->zoomFactor());
    x = m_data->x + ((m_data->width/2) - (w/2));
    y = m_data->y + ((m_data->height/2) - (h/2));
    int currentFrame = (m_data->endFrame - m_data->startFrame) * t + m_data->startFrame;
    game->renderer->drawAnimQuad(x, y,
                                 w, h,
                                 m_data->texture, m_data->flip, currentFrame
    );
    game->popZoomMatrix();
  }

    void DrawScreenText::animate(const float &t, AnimData *d, IGame *game)
    {
      if(game->options->getNumber("Toggle Talk") > 0.0f)
      {
        DrawFadedObject::animate(t, d, game);

        game->pushZoomMatrix();
        float fontSize = 150.0f * (1/game->zoomFactor());
        string text = m_data->text;
        float textWidth = game->renderer->textWidth("Roboto", text, fontSize);
        textWidth *= (1/game->zoomFactor());

        float x,y, w, h;
        w = m_data->width * (1/game->zoomFactor());
        h = m_data->height * (1/game->zoomFactor());
        x = m_data->x + ((m_data->width/2) - (w/2)) - ((textWidth/2) * 40); //(game->renderer->textWidth("Roboto", text, 100.0f)/2);
        y = m_data->y + ((m_data->height/2) - (h/2)) - ((1/game->zoomFactor()) * 40);



        game->renderer->drawText(x, y, "Roboto", text, fontSize);
        //game->renderer->drawTexturedQuad(x, y, w, h, 1.0f, m_data->texture, m_data->flip );
        game->popZoomMatrix();
      }
    }
}
